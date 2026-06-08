import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


dice10 = list(range(1, 11))
dice6 = list(range(1, 7))
all_weapons = ["SRM2", "SRM4", "SRM6", "LRM10", "LRM15", "LRM20"]
all_trefferzone = ["vorne", "rechts", "links"]


def hit_calculator(shot_count, trefferwurf):
    hit_counter = 0
    for shot in range(shot_count):
        dice_sum = random.choice(dice10) + random.choice(dice10)
        if dice_sum >= trefferwurf:
            hit_counter += 1
    return hit_counter


def missel_count(hit_counter, waffe_typ):
    real_missel = 0
    while hit_counter > 0:
        hit_counter -= 1
        dice_sum = random.choice(dice6) + random.choice(dice6)
        if waffe_typ == "SRM2":
            if dice_sum <= 7:
                real_missel += 1
            else:
                real_missel += 2
        elif waffe_typ == "SRM4":
            if dice_sum == 2:
                real_missel += 1
            elif dice_sum <= 7:
                real_missel += 2
            else:
                real_missel += 3 if dice_sum <= 9 else 4
        elif waffe_typ == "SRM6":
            if dice_sum <= 3:
                real_missel += 2
            elif dice_sum <= 5:
                real_missel += 3
            elif dice_sum <= 8:
                real_missel += 4
            elif dice_sum <= 10:
                real_missel += 5
            else:
                real_missel += 6
        elif waffe_typ == "LRM10":
            if dice_sum <= 3:
                real_missel += 3
            elif dice_sum == 4:
                real_missel += 4
            elif dice_sum <= 8:
                real_missel += 6
            elif dice_sum <= 10:
                real_missel += 8
            else:
                real_missel += 10
        elif waffe_typ == "LRM15":
            if dice_sum <= 3:
                real_missel += 5
            elif dice_sum == 4:
                real_missel += 6
            elif dice_sum <= 8:
                real_missel += 9
            elif dice_sum <= 10:
                real_missel += 12
            else:
                real_missel += 15
        elif waffe_typ == "LRM20":
            if dice_sum <= 3:
                real_missel += 6
            elif dice_sum == 4:
                real_missel += 9
            elif dice_sum <= 8:
                real_missel += 12
            elif dice_sum <= 10:
                real_missel += 16
            else:
                real_missel += 20
    return real_missel


def hit_location_summary(hit_counter, srm, zone):
    zones = {
        "vorne": {
            2: ("Center Torso Kritisch", "ct_crit"),
            3: ("Rechter Arm", "ra"),
            4: ("Rechter Arm", "ra"),
            5: ("Rechtes Bein", "rl"),
            6: ("Rechter Torso", "rt"),
            7: ("Center Torso", "ct"),
            8: ("Linker Torso", "lt"),
            9: ("Linkes Bein", "ll"),
            10: ("Linker Arm", "la"),
            11: ("Linker Arm", "la"),
            12: ("Kopf", "hd"),
        },
        "links": {
            2: ("Linker Torso Kritisch", "lt_crit"),
            3: ("Linkes Bein", "ll"),
            4: ("Linker Arm", "la"),
            5: ("Linker Arm", "la"),
            6: ("Linkes Bein", "ll"),
            7: ("Linker Torso", "lt"),
            8: ("Center Torso", "ct"),
            9: ("Rechter Torso", "rt"),
            10: ("Rechter Arm", "ra"),
            11: ("Rechtes Bein", "rl"),
            12: ("Kopf", "hd"),
        },
        "rechts": {
            2: ("Rechter Torso Kritisch", "rt_crit"),
            3: ("Rechtes Bein", "rl"),
            4: ("Rechter Arm", "ra"),
            5: ("Rechter Arm", "ra"),
            6: ("Rechtes Bein", "rl"),
            7: ("Rechter Torso", "rt"),
            8: ("Center Torso", "ct"),
            9: ("Linker Torso", "lt"),
            10: ("Linker Arm", "la"),
            11: ("Linkes Bein", "ll"),
            12: ("Kopf", "hd"),
        },
    }

    counts = {
        "hd": 0,
        "rl": 0,
        "ra": 0,
        "rt": 0,
        "ct": 0,
        "lt": 0,
        "ll": 0,
        "la": 0,
        "ct_crit": 0,
        "lt_crit": 0,
        "rt_crit": 0,
    }

    if zone not in zones:
        return "Ungültige Trefferzone"

    mapping = zones[zone]
    for _ in range(hit_counter):
        dice_sum = random.choice(dice6) + random.choice(dice6)
        key = mapping[dice_sum][1]
        counts[key] += 1

    lines = []
    if counts["hd"]:
        lines.append(f"Kopf: {counts['hd']} {srm}")
    if counts["rl"]:
        lines.append(f"Rechtes Bein: {counts['rl']} {srm}")
    if counts["ll"]:
        lines.append(f"Linkes Bein: {counts['ll']} {srm}")
    if counts["ra"]:
        lines.append(f"Rechter Arm: {counts['ra']} {srm}")
    if counts["rt"]:
        lines.append(f"Rechter Torso: {counts['rt']} {srm}")
    if counts["ct"]:
        lines.append(f"Center Torso: {counts['ct']} {srm}")
    if counts["lt"]:
        lines.append(f"Linker Torso: {counts['lt']} {srm}")
    if counts["la"]:
        lines.append(f"Linker Arm: {counts['la']} {srm}")
    if counts["ct_crit"]:
        lines.append(f"Center Torso Kritisch: {counts['ct_crit']} {srm}")
    if counts["lt_crit"]:
        lines.append(f"Linker Torso Kritisch: {counts['lt_crit']} {srm}")
    if counts["rt_crit"]:
        lines.append(f"Rechter Torso Kritisch: {counts['rt_crit']} {srm}")

    if not lines:
        lines.append("Keine Trefferzonenwürfe")

    return "\n".join(lines)


class GuiCalcApp(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=10, spacing=10)

        form = GridLayout(cols=2, spacing=10, size_hint_y=None)
        form.bind(minimum_height=form.setter("height"))

        form.add_widget(Label(text="Waffentyp:"))
        self.weapon_spinner = Spinner(text="SRM2", values=all_weapons)
        form.add_widget(self.weapon_spinner)

        form.add_widget(Label(text="Anzahl Waffen:"))
        self.shot_input = TextInput(text="1", multiline=False, input_filter="int")
        form.add_widget(self.shot_input)

        form.add_widget(Label(text="Trefferwert:"))
        self.target_input = TextInput(text="8", multiline=False, input_filter="int")
        form.add_widget(self.target_input)

        form.add_widget(Label(text="Trefferzone:"))
        self.zone_spinner = Spinner(text="vorne", values=all_trefferzone)
        form.add_widget(self.zone_spinner)

        root.add_widget(form)

        self.result_label = Label(text="Bereit zur Berechnung.", halign="left", valign="top")
        self.result_label.bind(size=self._update_text_size)
        root.add_widget(self.result_label)

        self.calculate_button = Button(text="Feuer frei!", size_hint_y=None, height=50)
        self.calculate_button.bind(on_release=self.calculate)
        root.add_widget(self.calculate_button)

        return root

    def _update_text_size(self, instance, value):
        instance.text_size = (value[0] - 20, None)

    def calculate(self, instance):
        try:
            shot_count = int(self.shot_input.text)
            trefferwurf = int(self.target_input.text)
        except ValueError:
            self.result_label.text = "Bitte gültige ganze Zahlen eingeben."
            return

        weapon = self.weapon_spinner.text
        zone = self.zone_spinner.text
        srm = "Treffer"
        if weapon in {"SRM2", "SRM4", "SRM6"}:
            srm = "Treffer x2 Dmg"

        hit_counter = hit_calculator(shot_count, trefferwurf)
        real_missel = missel_count(hit_counter, weapon)
        location_text = hit_location_summary(real_missel, srm, zone)

        self.result_label.text = (
            f"Treffer: {hit_counter} von {shot_count}\n"
            f"Raketen insgesamt: {real_missel}\n"
            f"Trefferzone: {zone}\n\n"
            f"{location_text}"
        )


if __name__ == "__main__":
    GuiCalcApp().run()
