
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp


class SafeGuardAI(App):

    def build(self):
        self.title = "SafeGuard AI"

        root = BoxLayout(
            orientation="vertical",
            padding=dp(25),
            spacing=dp(20)
        )

        with root.canvas.before:
            Color(0.025, 0.045, 0.09, 1)
            self.bg = RoundedRectangle(
                pos=root.pos,
                size=root.size
            )

        root.bind(pos=lambda i, v: setattr(self.bg, "pos", v))
        root.bind(size=lambda i, v: setattr(self.bg, "size", v))

        root.add_widget(Label(size_hint_y=0.3))

        root.add_widget(Label(
            text="[b]SafeGuard AI[/b]",
            markup=True,
            font_size="32sp",
            color=(0.2, 0.8, 1, 1),
            size_hint_y=None,
            height=dp(70)
        ))

        root.add_widget(Label(
            text="Mobile Security System",
            font_size="17sp",
            color=(0.8, 0.85, 0.95, 1)
        ))

        self.status = Label(
            text="Protection is ready",
            font_size="18sp",
            color=(0.2, 1, 0.65, 1)
        )
        root.add_widget(self.status)

        btn = Button(
            text="Run Security Test",
            size_hint=(1, None),
            height=dp(60),
            background_normal="",
            background_color=(0.05, 0.45, 0.8, 1),
            font_size="18sp"
        )

        btn.bind(on_press=self.test)
        root.add_widget(btn)

        root.add_widget(Label(
            text="AI engine integration pending",
            font_size="14sp",
            color=(0.65, 0.7, 0.8, 1)
        ))

        root.add_widget(Label(size_hint_y=0.3))

        return root

    def test(self, instance):
        self.status.text = "Interface test successful"


if __name__ == "__main__":
    SafeGuardAI().run()

