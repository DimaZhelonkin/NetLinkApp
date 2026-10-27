import json
import os
import socket
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Файл для保存 настроек
CONFIG_FILE = "config.json"

# Реальный IP вашего компьютера (подставляем ваш рабочий IP)
REAL_PC_IP = "192.168.1.180"
LOCAL_IP = "127.0.0.1"
SERVER_PORT = 65432

Window.clearcolor = (0.035, 0.035, 0.039, 1)  # #09090A


class NetLink2ndApp(App):

    def build(self):
        self.title = "NETLINK_2ND // Мобильный Клиент"

        # Загружаем сохраненный режим из JSON
        self.current_mode = self.load_mode_from_json()

        # Главный контейнер
        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)

        # 1. Текстовое поле для вывода чисел и ошибок
        self.result_label = Label(
            text="СИСТЕМА: СВЯЗЬ ГОТОВА\n[ НАЖМИТЕ КНОПКУ ДЛЯ ЗАПРОСА ]",
            font_size="20sp",
            font_name="Roboto",
            color=(0.015, 0.827, 0.380, 1),  # Неоново-зеленый
            halign="center",
            valign="middle",
            size_hint=(1, 0.5),
        )
        self.result_label.bind(size=self.result_label.setter("text_size"))

        # 2. КНОПКА ПЕРЕКЛЮЧЕНИЯ РЕЖИМА (Локальный / Wi-Fi)
        self.mode_btn = Button(
            text="",  # Текст обновится ниже
            font_size="14sp",
            font_name="Roboto",
            size_hint=(1, 0.15),
            background_normal="",
        )
        self.mode_btn.bind(on_press=self.toggle_mode)
        self.update_mode_button_ui()  # Настраиваем внешний вид кнопки при старте

        # 3. КНОПКА ЗАПРОСА ЧИСЛА
        request_btn = Button(
            text="[ ЗАПРОСИТЬ ЧИСЛО ИИ ]",
            font_size="18sp",
            font_name="Roboto",
            size_hint=(1, 0.35),
            background_normal="",
            background_color=(0.015, 0.827, 0.380, 1),
            color=(0, 0, 0, 1),
        )
        request_btn.bind(on_press=self.send_request_to_pc)

        # Собираем все элементы на экран
        layout.add_widget(self.result_label)
        layout.add_widget(self.mode_btn)
        layout.add_widget(request_btn)

        return layout

    def on_stop(self):
        """ЖЕЛЕЗНАЯ ЗАЩИТА: Срабатывает при закрытии окна на крестик."""
        import os

        os._exit(0)  # Полностью уничтожает процесс в памяти компьютера

    def get_current_ip(self):
        """Возвращает IP в зависимости от выбранного режима."""
        if self.current_mode == "wifi":
            return REAL_PC_IP
        return LOCAL_IP

    def toggle_mode(self, instance):
        """Переключает режим по нажатию кнопки и сохраняет в JSON."""
        if self.current_mode == "local":
            self.current_mode = "wifi"
        else:
            self.current_mode = "local"

        self.save_mode_to_json(self.current_mode)
        self.update_mode_button_ui()

    def update_mode_button_ui(self):
        """Обновляет текст и цвет кнопки переключения режима."""
        if self.current_mode == "wifi":
            self.mode_btn.text = f"РЕЖИМ: WI-FI СЕТЬ ({REAL_PC_IP})"
            self.mode_btn.background_color = (0.2, 0.6, 1, 1)  # Синий кибер-цвет
            self.mode_btn.color = (1, 1, 1, 1)
        else:
            self.mode_btn.text = f"РЕЖИМ: ОБМАНКА ({LOCAL_IP})"
            self.mode_btn.background_color = (
                0.3,
                0.3,
                0.35,
                1,
            )  # Темно-серый цвет
            self.mode_btn.color = (0.8, 0.8, 0.8, 1)

    def send_request_to_pc(self, instance):
        """Отправка сетевого запроса."""
        target_ip = self.get_current_ip()
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2.0)
                s.connect((target_ip, SERVER_PORT))
                s.sendall(b"get_number")
                response = s.recv(1024).decode("utf-8")
                self.result_label.text = (
                    f"ДАННЫЕ ПОЛУЧЕНЫ:\nИИ_ЧИСЛО: [{response}]"
                )
        except socket.timeout:
            self.result_label.text = (
                f"ОШИБКА: ТАЙМАУТ СВЯЗИ\nПроверьте IP: {target_ip}"
            )
        except Exception as e:
            self.result_label.text = (
                f"СБОЙ ПОДКЛЮЧЕНИЯ к {target_ip}:\n{str(e)}"
            )

    def load_mode_from_json(self):
        """Загрузка настроек из JSON файла."""
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    data = json.load(f)
                    return data.get("mode", "local")
            except:
                return "local"
        return "local"

    def save_mode_to_json(self, mode):
        """Сохранение настроек в JSON файл."""
        try:
            with open(CONFIG_FILE, "w") as f:
                json.dump({"mode": mode}, f, indent=4)
        except Exception as e:
            print(f"Не удалось сохранить конфиг: {e}")


if __name__ == "__main__":
    NetLink2ndApp().run()
