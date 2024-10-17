import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr
from math import sin, cos
import random

# Sphere generation using parametric equations
def create_sphere(radius, lat_steps, lon_steps):
    vertices = []
    normals = []
    indices = []

    for i in range(lat_steps + 1):
        theta = np.pi * i / lat_steps
        sin_theta = sin(theta)
        cos_theta = cos(theta)

        for j in range(lon_steps + 1):
            phi = 2 * np.pi * j / lon_steps
            sin_phi = sin(phi)
            cos_phi = cos(phi)

            x = cos_phi * sin_theta
            y = cos_theta
            z = sin_phi * sin_theta

            vertices.append([radius * x, radius * y, radius * z])
            normals.append([x, y, z])

    for i in range(lat_steps):
        for j in range(lon_steps):
            first = i * (lon_steps + 1) + j
            second = first + lon_steps + 1

            indices.append(first)
            indices.append(second)
            indices.append(first + 1)

            indices.append(second)
            indices.append(second + 1)
            indices.append(first + 1)

    return np.array(vertices, dtype=np.float32), np.array(normals, dtype=np.float32), np.array(indices, dtype=np.uint32)

# Vertex Shader (GLSL 1.20)
vertex_shader = """
#version 120

attribute vec3 position;
attribute vec3 normal;

varying vec3 FragPos;
varying vec3 Normal;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main() {
    FragPos = vec3(model * vec4(position, 1.0));
    Normal = mat3(transpose(model)) * normal;
    gl_Position = projection * view * vec4(FragPos, 1.0);
}
"""

# Fragment Shader (GLSL 1.20)
fragment_shader = """
#version 120

varying vec3 FragPos;
varying vec3 Normal;

uniform vec3 lightPos;
uniform vec3 viewPos;
uniform vec3 lightColor;
uniform vec3 objectColor;
uniform float metallic;
uniform float specularStrength;

void main() {
    // Ambient
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;

    // Diffuse
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    // Specular
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 16.0);
    vec3 specular = specularStrength * spec * lightColor;

    vec3 result = (ambient + diffuse + specular * metallic) * objectColor;
    gl_FragColor = vec4(result, 1.0);
}
"""

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Set fullscreen display
    monitor = glfw.get_primary_monitor()
    video_mode = glfw.get_video_mode(monitor)

    # Access the width and height from video_mode
    width, height = video_mode.size.width, video_mode.size.height

    window = glfw.create_window(width, height, "OpenGL Spheres Grid", monitor, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Compile shaders and link them into a program
    shader = compileProgram(compileShader(vertex_shader, GL_VERTEX_SHADER),
                            compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    # Generate the sphere
    sphere_vertices, sphere_normals, sphere_indices = create_sphere(1.0, 40, 40)

    # Create VBOs (one for vertices, one for normals) and EBO
    vbo = glGenBuffers(2)
    ebo = glGenBuffers(1)

    # Vertex buffer for positions
    glBindBuffer(GL_ARRAY_BUFFER, vbo[0])
    glBufferData(GL_ARRAY_BUFFER, sphere_vertices.nbytes, sphere_vertices, GL_STATIC_DRAW)

    # Vertex buffer for normals
    glBindBuffer(GL_ARRAY_BUFFER, vbo[1])
    glBufferData(GL_ARRAY_BUFFER, sphere_normals.nbytes, sphere_normals, GL_STATIC_DRAW)

    # Element buffer for indices
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sphere_indices.nbytes, sphere_indices, GL_STATIC_DRAW)

    glEnable(GL_DEPTH_TEST)



    # Uniform locations
    model_loc = glGetUniformLocation(shader, "model")
    view_loc = glGetUniformLocation(shader, "view")
    projection_loc = glGetUniformLocation(shader, "projection")
    light_pos_loc = glGetUniformLocation(shader, "lightPos")
    view_pos_loc = glGetUniformLocation(shader, "viewPos")
    light_color_loc = glGetUniformLocation(shader, "lightColor")
    object_color_loc = glGetUniformLocation(shader, "objectColor")
    metallic_loc = glGetUniformLocation(shader, "metallic")
    specular_strength_loc = glGetUniformLocation(shader, "specularStrength")

    # Set the projection matrix
    projection = pyrr.matrix44.create_perspective_projection(45, video_mode.size.width / video_mode.size.height, 0.1, 50, dtype=np.float32)
    
    # Light properties
    light_pos = pyrr.vector3.create(5, 5, 5, dtype=np.float32)
    light_color = np.array([1.0, 1.0, 1.0], dtype=np.float32)

    # Random rotation directions for each sphere
    rotation_speeds = {(i, j): random.uniform(0.5, 2.0) for i in range(-2, 3) for j in range(-2, 3)}

    # Camera movement variables
    camera_pos = pyrr.vector3.create(5, 5, 10)
    move_speed = 0.1

    while not glfw.window_should_close(window):
        glfw.poll_events()

        # Handle camera movement with arrow keys
        if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
            camera_pos[1] += move_speed
        if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
            camera_pos[1] -= move_speed
        if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            camera_pos[0] -= move_speed
        if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
            camera_pos[0] += move_speed

        # Exit on pressing 'Q'
        if glfw.get_key(window, glfw.KEY_Q) == glfw.PRESS:
            break

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUseProgram(shader)

        # Camera and transformation matrices
        view = pyrr.matrix44.create_look_at(camera_pos, pyrr.vector3.create(0, 0, 0), pyrr.vector3.create(0, 1, 0), dtype=np.float32)
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
        glUniformMatrix4fv(projection_loc, 1, GL_FALSE, projection)
        glUniform3fv(light_pos_loc, 1, light_pos)
        glUniform3fv(light_color_loc, 1, light_color)
        glUniform3fv(view_pos_loc, 1, camera_pos)

        # Render multiple spheres in a grid with different material properties
        for i in range(-2, 3):
            for j in range(-2, 3):
                # Model matrix (rotate and translate each sphere with random rotation direction)
                rotation_angle = glfw.get_time() * rotation_speeds[(i, j)]
                model = pyrr.matrix44.create_from_translation(pyrr.vector3.create(i * 2.5, j * 2.5, 0), dtype=np.float32)
                model = pyrr.matrix44.multiply(model, pyrr.matrix44.create_from_y_rotation(rotation_angle, dtype=np.float32))
                glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)

                # Set different material properties for each sphere
                metallic = (i + 2) / 4.0  # Varies from 0 to 1
                specular_strength = (j + 2) / 4.0  # Varies from 0 to 1
                glUniform1f(metallic_loc, metallic)
                glUniform1f(specular_strength_loc, specular_strength)

                # Set object color (vary it slightly)
                glUniform3f(object_color_loc, 0.7, 0.2 + j * 0.1, 0.3)

                # Draw the sphere
                glBindBuffer(GL_ARRAY_BUFFER, vbo[0])
                glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
                glEnableVertexAttribArray(0)

                glBindBuffer(GL_ARRAY_BUFFER, vbo[1])
                glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
                glEnableVertexAttribArray(1)

                glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
                glDrawElements(GL_TRIANGLES, len(sphere_indices), GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
