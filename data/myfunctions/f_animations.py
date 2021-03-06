# animation functions

# imports
from Tkinter import ALL
from tkMessageBox import askquestion
from time import time
from math import pi, sin, cos

from f_other import dtr, GrayScale
from f_programconfig import setRadiusFalse, setAngVelFalse

from data.myvariables import dev, ask_again_list, spoke_step, platform_width, part_radius, circum_width
from data.myvariables import ask_radius_error_bool as areb
from data.myvariables import ask_ang_vel_error_bool as aaveb

# assigning imported variables to global variables
ask_radius_error_bool = areb
ask_ang_vel_error_bool = aaveb


# line at theta degrees from x_pos, y_pos to x, y (for animate_rotating_circle)
def ttl(canvas, x_pos, y_pos, radius, theta):
    x = x_pos + (float(radius) * sin(dtr(theta)))
    y = y_pos + (float(-radius) * cos(dtr(theta)))
    return canvas.create_line(x_pos, y_pos, x, y, fill=GrayScale(220))


# warning tuples
radius_error_list = ['Run Animation Anyway?',
                     'You have selected a radius value which may cause parts of the animation to be be invisible.'
                     '\nIt is recommended to reduce Length Multiplier in animation settings.'
                     '\nDo you want to run the animation anyway?']

ang_vel_error_list = ['Run Animation Anyway?',
                      'You have selected an angular velocity value which may cause the animation speed to be inaccurate.'
                      '\nIt is recommended to increase Time Factor in animation settings '
                      '\nDo you want to run the animation anyway?']


# animate orbiting particle
def orbiting_particle_animation(root, canvas, x_pos, y_pos, radius, ang_vel, granularity):
    global ask_radius_error_bool, ask_ang_vel_error_bool
    # checking value ranges
    if radius >= 180 and ask_radius_error_bool:
        radius_error = askquestion(radius_error_list[0], radius_error_list[1])
        if radius_error == 'no':
            return

        else:
            radius_error_ask = askquestion(ask_again_list[0], ask_again_list[1])

            if radius_error_ask == 'yes':
                ask_radius_error_bool = False
                setRadiusFalse()

    if ang_vel >= 10 and ask_ang_vel_error_bool:
        ang_vel_error = askquestion(ang_vel_error_list[0], ang_vel_error_list[1])

        if ang_vel_error == 'no':
            return

        else:
            ang_vel_error_ask = askquestion(ask_again_list[0], ask_again_list[1])

            if ang_vel_error_ask == 'yes':
                ask_ang_vel_error_bool = False
                setAngVelFalse()

    # angular frequency defined as angular velocity / 2pi
    ang_freq = ang_vel / (2 * pi)

    # clearing canvas
    canvas.delete(ALL)

    # center_particle
    canvas.create_oval(x_pos - part_radius,
                       y_pos - part_radius,
                       x_pos + part_radius,
                       y_pos + part_radius,
                       fill=GrayScale(220)
                       )

    # orbit_path
    canvas.create_oval(x_pos - radius,
                       y_pos - radius,
                       x_pos + radius,
                       y_pos + radius,
                       outline=GrayScale(220)
                       )

    # orbiting particle
    while True:
        old_time = 0
        for theta in range(0, 360, int(granularity)):
            c_start = time()

            ref_ms = int(1000 * ((1.0 / float(ang_freq)) / (360.0 / float(granularity))))
            x = x_pos + (float(radius) * sin(dtr(theta)))
            y = y_pos + (float(-radius) * cos(dtr(theta)))
            orb_part = canvas.create_oval(x - part_radius,
                                          y - part_radius,
                                          x + part_radius,
                                          y + part_radius,
                                          fill=GrayScale(220)
                                          )
            canvas.update()
            root.after(ref_ms, canvas.delete(orb_part))

            c_end = time()
            new_time = c_end - c_start

            if dev and round(new_time, 2) != round(old_time, 2):
                print '[animation] time per cycle', round(new_time, 2)

            old_time = new_time


# animate rotating circle
def rotating_circle_animation(root,
                              canvas,
                              x_pos,
                              y_pos,
                              radius,
                              ang_vel,
                              granularity):
    global ask_radius_error_bool, ask_ang_vel_error_bool
    # checking value ranges
    if radius >= 200 and ask_radius_error_bool:
        radius_error = askquestion(radius_error_list[0], radius_error_list[1])
        if radius_error == 'no':
            return

        else:
            radius_error_ask = askquestion(ask_again_list[0], ask_again_list[1])

            if radius_error_ask == 'yes':
                ask_radius_error_bool = False
                setRadiusFalse()

    if ang_vel >= 10 and ask_ang_vel_error_bool:
        ang_vel_error = askquestion(ang_vel_error_list[0], ang_vel_error_list[1])

        if ang_vel_error == 'no':
            return

        else:
            ang_vel_error_ask = askquestion(ask_again_list[0], ask_again_list[1])

            if ang_vel_error_ask == 'yes':
                ask_ang_vel_error_bool = False
                setAngVelFalse()

    # angular frequency defined as angular velocity / 2pi
    ang_freq = ang_vel / (2 * pi)

    # clearing canvas
    canvas.delete(ALL)

    # circumference
    canvas.create_oval(x_pos - radius,
                       y_pos - radius,
                       x_pos + radius,
                       y_pos + radius,
                       width=circum_width,
                       outline=GrayScale(220)
                       )

    # center
    canvas.create_oval(x_pos - (float(radius) / 50.0),
                       y_pos - (float(radius) / 50.0),
                       x_pos + (float(radius) / 50.0),
                       y_pos + (float(radius) / 50.0),
                       width=circum_width,
                       fill=GrayScale(220)
                       )

    while True:
        old_time = 0
        for theta in range(0, 360, int(granularity)):
            c_start = time()

            ref_ms = int(1000 * ((1.0 / float(ang_freq)) / (360.0 / float(granularity))))

            line1 = ttl(canvas, x_pos, y_pos, radius, theta + (0 * spoke_step))
            line2 = ttl(canvas, x_pos, y_pos, radius, theta + (1 * spoke_step))
            line3 = ttl(canvas, x_pos, y_pos, radius, theta + (2 * spoke_step))
            line4 = ttl(canvas, x_pos, y_pos, radius, theta + (3 * spoke_step))

            canvas.update()
            root.after(ref_ms, canvas.delete(line1, line2, line3, line4))

            c_end = time()
            new_time = c_end - c_start

            if dev and round(new_time, 2) != round(old_time, 2):
                print '[animation] time per cycle', round(new_time, 2)

            old_time = new_time


# animate rolling circle
def rolling_circle_animation(root,
                             canvas,
                             x_pos,
                             y_pos,
                             radius,
                             ang_vel,
                             granularity
                             ):
    global ask_radius_error_bool, ask_ang_vel_error_bool
    # checking value ranges
    if radius >= 200 and ask_radius_error_bool:
        radius_error = askquestion(radius_error_list[0], radius_error_list[1])
        if radius_error == 'no':
            return

        else:
            radius_error_ask = askquestion(ask_again_list[0], ask_again_list[1])

            if radius_error_ask == 'yes':
                ask_radius_error_bool = False
                setRadiusFalse()

    if ang_vel >= 10 and ask_ang_vel_error_bool:
        ang_vel_error = askquestion(ang_vel_error_list[0], ang_vel_error_list[1])

        if ang_vel_error == 'no':
            return

        else:
            ang_vel_error_ask = askquestion(ask_again_list[0], ask_again_list[1])

            if ang_vel_error_ask == 'yes':
                ask_ang_vel_error_bool = False
                setAngVelFalse()

    circumference = 2.0 * pi * float(radius)
    ang_freq = ang_vel / (2 * pi)
    arc_len = float(granularity) / 360.0 * float(circumference)

    line_step = int(radius)

    ref_ms = int(1000 * ((1.0 / float(ang_freq)) / (360.0 / float(granularity))))

    px_pos = x_pos - (2 * float(radius))
    py_pos = y_pos + radius + (0.5 * circum_width)
    platform_len = 4.0 * float(radius)
    platform_thickness = float(platform_len) / 10.0

    # clearing canvas
    canvas.delete(ALL)

    rec_num = 0

    while True:
        old_time = 0
        for theta in range(0, 360, int(granularity)):
            c_start = time()

            # circumference
            canvas.create_oval(x_pos - radius,
                               y_pos - radius,
                               x_pos + radius,
                               y_pos + radius,
                               width=circum_width,
                               outline=GrayScale(220)
                               )

            # center
            canvas.create_oval(x_pos - (float(radius) / 50.0),
                               y_pos - (float(radius) / 50.0),
                               x_pos + (float(radius) / 50.0),
                               y_pos + (float(radius) / 50.0),
                               width=circum_width,
                               fill=GrayScale(220)
                               )

            # platform outline
            canvas.create_rectangle(px_pos,
                                    py_pos,
                                    px_pos + platform_len,
                                    py_pos + platform_thickness,
                                    width=platform_width,
                                    outline=GrayScale(220)
                                    )

            # rotating spokes
            for line_theta in range(theta, theta + 360, int(spoke_step)):
                ttl(canvas, x_pos, y_pos, radius, line_theta)

            # moving platform
            rec_num += 1

            line_xpos = px_pos + platform_len - (rec_num * arc_len)

            # checking line_xpos validity and correcting if invalid
            if line_xpos <= px_pos + platform_len - line_step:
                rec_num = 0
                line_xpos = px_pos + platform_len - (rec_num * arc_len)

            # drawing vertical platform lines
            for line_pos in range(int(line_xpos), int(px_pos), -line_step):
                canvas.create_line(line_pos, py_pos, line_pos, py_pos + platform_thickness, fill=GrayScale(220))

            # refreshing the canvas with all components drawn
            canvas.update()

            # deleting all components after ref_ms
            root.after(ref_ms, canvas.delete(ALL))

            c_end = time()
            new_time = c_end - c_start

            if dev and round(new_time, 2) != round(old_time, 2):
                print '[animation] time per cycle', round(new_time, 2)

            old_time = new_time
