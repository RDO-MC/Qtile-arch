import os
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "kitty"

keys = [
     # ... tus otras teclas ...
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q sset Master toggle")),

     Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    
        # Volumen
    Key([mod], "F11", lazy.spawn("pamixer -i 5"), desc="Subir volumen"),
    Key([mod], "F10", lazy.spawn("pamixer -d 5"), desc="Bajar volumen"),
    Key([mod], "F9", lazy.spawn("pamixer -t"), desc="Mute/Unmute volumen"),

    # Brillo
    Key([mod], "F4", lazy.spawn("brightnessctl s +10%"), desc="Aumentar brillo"),
    Key([mod], "F3", lazy.spawn("brightnessctl s 10%-"), desc="Disminuir brillo"),

    # ... tus otras configuraciones de teclas

    Key([mod], "Return", lazy.spawn("kitty -o include ~/.config/kitty/kitty.conf"), desc="Launch Kitty with Qtile config"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch firefox browser"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Launch Rofi application launcher"),
    Key([mod], "f", lazy.spawn("kitty -e ranger"), desc="Launch Ranger file manager in Kitty terminal"),
    Key([mod], "m", lazy.spawn("~/.config/cmatrix/run_cmatrix.sh"), desc="Run cmatrix with custom settings"),

]

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Matrix(),
]

widget_defaults = dict(
    font="sans",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
      #  top=bar.Bar(
       #     [
        #        widget.CurrentLayout(),
               # widget.Prompt(),
               # widget.WindowName(),
                #widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
               # widget.Battery(),
               # widget.CPU(),
               # widget.Memory(),
                #widget.PulseVolume(),
           # ],
           # 24,
        #),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

autostart = [
    "setxkbmap es",
    "feh --bg-fill /home/acdc/.config/qtile/woman.jpg",
    "xcompmgr &",
    "picom &",
    "nm-applet &",
    "pulseaudio --start",
    "polybar -rq bar &",
    "brightnessctl &",
    "alsa-utils &"
]

for x in autostart:
    os.system(x)
