from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton

KV = '''
ScreenManager:
    StartScreen:
    WelcomeScreen:
    TransactionScreen:
    BalanceScreen:
    WithdrawScreen:
    DepositScreen:
    HistoryScreen:

<CustomButton@MDRaisedButton>:
    md_bg_color: app.theme_cls.primary_color

<StartScreen>:
    name: 'start'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'atm_logo.png'  # Path to your image file
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        CustomButton:
            text: "Insert Card"
            pos_hint: {"center_x": 0.5}
            on_release: app.insert_card()

<WelcomeScreen>:
    name: 'welcome'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDLabel:
            text: "Welcome to ATM"
            halign: 'center'
            font_style: 'H4'
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1
        MDTextField:
            id: pin_input
            hint_text: "Enter PIN"
            password: True
            mode: "rectangle"
            multiline: False
            current_hint_text_color: 0, 1, 0, 1
            hint_text_color_normal: 0, 1, 0, 1
        MDGridLayout:
            cols: 3
            rows: 4
            spacing: dp(10)
            CustomButton:
                text: "1"
                on_release: app.update_pin_input('1')
            CustomButton:
                text: "2"
                on_release: app.update_pin_input('2')
            CustomButton:
                text: "3"
                on_release: app.update_pin_input('3')
            CustomButton:
                text: "4"
                on_release: app.update_pin_input('4')
            CustomButton:
                text: "5"
                on_release: app.update_pin_input('5')
            CustomButton:
                text: "6"
                on_release: app.update_pin_input('6')
            CustomButton:
                text: "7"
                on_release: app.update_pin_input('7')
            CustomButton:
                text: "8"
                on_release: app.update_pin_input('8')
            CustomButton:
                text: "9"
                on_release: app.update_pin_input('9')
            CustomButton:
                text: "Clear"
                on_release: app.clear_pin_input()
            CustomButton:
                text: "0"
                on_release: app.update_pin_input('0')
            CustomButton:
                text: "Enter"
                on_release: app.enter_pin()
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            CustomButton:
                text: "Exit"
                on_release: app.exit_app()
            MDLabel:
                id: message
                text: ""
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0, 1, 0, 1

<TransactionScreen>:
    name: 'transaction'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDLabel:
            text: "Transaction Options"
            halign: 'center'
            font_style: 'H4'
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1
        CustomButton:
            text: "Check Balance"
            on_release: app.go_to_balance()
        CustomButton:
            text: "Withdraw Cash"
            on_release: app.go_to_withdraw()
        CustomButton:
            text: "Deposit Cash"
            on_release: app.go_to_deposit()
        CustomButton:
            text: "Transaction History"
            on_release: app.go_to_history()
        CustomButton:
            text: "Exit"
            on_release: app.exit_to_welcome()
        CustomButton:
            text: "Close App"
            on_release: app.exit_app()

<BalanceScreen>:
    name: 'balance'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDLabel:
            id: balance_label
            text: ""
            halign: 'center'
            font_style: 'H4'
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1
        CustomButton:
            text: "Back"
            on_release: app.go_back_to_transaction()

<WithdrawScreen>:
    name: 'withdraw'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDTextField:
            id: withdraw_input
            hint_text: "Enter amount to withdraw"
            mode: "rectangle"
            multiline: False
            current_hint_text_color: 0, 1, 0, 1
            hint_text_color_normal: 0, 1, 0, 1
        CustomButton:
            text: "Withdraw"
            on_release: app.withdraw_cash()
        CustomButton:
            text: "Back"
            on_release: app.go_back_to_transaction()
        MDLabel:
            id: message
            text: ""
            halign: 'center'
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1

<DepositScreen>:
    name: 'deposit'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDTextField:
            id: deposit_input
            hint_text: "Enter amount to deposit"
            mode: "rectangle"
            multiline: False
            current_hint_text_color: 0, 1, 0, 1
            hint_text_color_normal: 0, 1, 0, 1
        CustomButton:
            text: "Deposit"
            on_release: app.deposit_cash()
        CustomButton:
            text: "Back"
            on_release: app.go_back_to_transaction()
        MDLabel:
            id: message
            text: ""
            halign: 'center'
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1

<HistoryScreen>:
    name: 'history'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDLabel:
            id: history_label
            text: ""
            halign: 'center'
            font_style: 'H4'
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1
        CustomButton:
            text: "Back"
            on_release: app.go_back_to_transaction()
'''

class StartScreen(Screen):
    pass

class WelcomeScreen(Screen):
    pass

class TransactionScreen(Screen):
    pass

class BalanceScreen(Screen):
    pass

class WithdrawScreen(Screen):
    pass

class DepositScreen(Screen):
    pass

class HistoryScreen(Screen):
    pass

class ATMApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.balance = 500000000
        self.transaction_history = []
        Window.bind(on_key_down=self._on_keyboard_down)
        return Builder.load_string(KV)

    def insert_card(self):
        self.root.current = 'welcome'

    def update_pin_input(self, value):
        current_text = self.root.get_screen('welcome').ids.pin_input.text
        self.root.get_screen('welcome').ids.pin_input.text = current_text + value

    def clear_pin_input(self):
        self.root.get_screen('welcome').ids.pin_input.text = ''

    def enter_pin(self):
        pin = self.root.get_screen('welcome').ids.pin_input.text
        if pin == '1234':
            self.root.current = 'transaction'
            self.root.get_screen('welcome').ids.pin_input.text = ''
            self.root.get_screen('welcome').ids.message.text = ''
        else:
            self.root.get_screen('welcome').ids.message.text = 'Incorrect PIN. Try again.'

    def go_to_balance(self):
        self.root.current = 'balance'
        self.root.get_screen('balance').ids.balance_label.text = f"Your balance is ${self.balance:.2f}"

    def go_to_withdraw(self):
        self.root.current = 'withdraw'

    def go_to_deposit(self):
        self.root.current = 'deposit'

    def go_to_history(self):
        self.root.current = 'history'
        history_text = "\n".join(self.transaction_history)
        self.root.get_screen('history').ids.history_label.text = history_text

    def go_back_to_transaction(self):
        self.root.current = 'transaction'

    def withdraw_cash(self):
        amount = float(self.root.get_screen('withdraw').ids.withdraw_input.text)
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
            self.root.get_screen('withdraw').ids.message.text = f"Successfully withdrew ${amount:.2f}"
        else:
            self.root.get_screen('withdraw').ids.message.text = "Insufficient balance"
        self.root.get_screen('withdraw').ids.withdraw_input.text = ''

    def deposit_cash(self):
        amount = float(self.root.get_screen('deposit').ids.deposit_input.text)
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount:.2f}")
        self.root.get_screen('deposit').ids.message.text = f"Successfully deposited ${amount:.2f}"
        self.root.get_screen('deposit').ids.deposit_input.text = ''

    def exit_to_welcome(self):
        self.root.current = 'welcome'

    def exit_app(self):
        self.stop()

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 8:  # Backspace key
            self.clear_pin_input()

if __name__ == '__main__':
    ATMApp().run()
