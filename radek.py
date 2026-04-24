import ast
import operator
import tkinter as tk
from tkinter import messagebox


class ExpressionEvaluator:
    """Bezpieczne obliczanie prostych wyrażeń matematycznych."""

    @classmethod
    def evaluate(cls, expression: str) -> float:
        cleaned_expression = expression.strip()
        if not cleaned_expression:
            raise ValueError("Wpisz działanie do obliczenia.")

        try:
            parsed_expression = ast.parse(cleaned_expression, mode="eval")
        except SyntaxError as error:
            raise ValueError("Niepoprawne wyrażenie.") from error

        return cls._evaluate_node(parsed_expression.body)

    @classmethod
    def _evaluate_node(cls, node: ast.AST) -> float:
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)

        if isinstance(node, ast.BinOp):
            left = cls._evaluate_node(node.left)
            right = cls._evaluate_node(node.right)

            if isinstance(node.op, ast.Add):
                operation = operator.add
            elif isinstance(node.op, ast.Sub):
                operation = operator.sub
            elif isinstance(node.op, ast.Mult):
                operation = operator.mul
            elif isinstance(node.op, ast.Div):
                operation = operator.truediv
            else:
                raise ValueError("Nieobsługiwany operator.")

            try:
                return operation(left, right)
            except ZeroDivisionError as error:
                raise ZeroDivisionError("Nie można dzielić przez zero.") from error

        if isinstance(node, ast.UnaryOp):
            operand = cls._evaluate_node(node.operand)

            if isinstance(node.op, ast.UAdd):
                operation = operator.pos
            elif isinstance(node.op, ast.USub):
                operation = operator.neg
            else:
                raise ValueError("Nieobsługiwany operator.")

            return operation(operand)

        raise ValueError("Dozwolone są tylko liczby oraz operatory +, -, *, / i nawiasy.")


class CalculatorApp:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Kalkulator Radek")
        self.window.geometry("360x460")
        self.window.resizable(False, False)
        self.window.configure(bg="#f2f2f2")

        self.expression_var = tk.StringVar()
        self.result_var = tk.StringVar(value="0")

        self._build_interface()
        self._bind_keyboard_shortcuts()

    def _build_interface(self) -> None:
        display_frame = tk.Frame(self.window, bg="#f2f2f2", padx=12, pady=12)
        display_frame.pack(fill="both")

        expression_entry = tk.Entry(
            display_frame,
            textvariable=self.expression_var,
            font=("Arial", 18),
            justify="right",
            bd=3,
            relief="groove",
        )
        expression_entry.pack(fill="x", pady=(0, 8))
        expression_entry.focus_set()

        result_label = tk.Label(
            display_frame,
            textvariable=self.result_var,
            anchor="e",
            bg="white",
            font=("Arial", 22, "bold"),
            bd=3,
            relief="groove",
            padx=10,
            pady=10,
        )
        result_label.pack(fill="x")

        buttons_frame = tk.Frame(self.window, bg="#f2f2f2", padx=12, pady=12)
        buttons_frame.pack(fill="both", expand=True)

        layout = [
            ["C", "(", ")", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "⌫", "="],
        ]

        for row_index, row in enumerate(layout):
            buttons_frame.grid_rowconfigure(row_index, weight=1)
            for column_index, button_text in enumerate(row):
                buttons_frame.grid_columnconfigure(column_index, weight=1)
                button = tk.Button(
                    buttons_frame,
                    text=button_text,
                    font=("Arial", 16, "bold"),
                    bd=1,
                    relief="raised",
                    command=lambda value=button_text: self._handle_button_click(value),
                )
                button.grid(
                    row=row_index,
                    column=column_index,
                    sticky="nsew",
                    padx=4,
                    pady=4,
                    ipadx=6,
                    ipady=12,
                )

    def _bind_keyboard_shortcuts(self) -> None:
        self.window.bind("<Return>", lambda _: self.calculate())
        self.window.bind("<KP_Enter>", lambda _: self.calculate())
        self.window.bind("<Escape>", lambda _: self.clear())
        self.window.bind("<BackSpace>", lambda _: self.backspace())

    def _handle_button_click(self, value: str) -> None:
        if value == "=":
            self.calculate()
        elif value == "C":
            self.clear()
        elif value == "⌫":
            self.backspace()
        else:
            self.expression_var.set(self.expression_var.get() + value)

    def clear(self) -> None:
        self.expression_var.set("")
        self.result_var.set("0")

    def backspace(self) -> None:
        self.expression_var.set(self.expression_var.get()[:-1])

    def calculate(self) -> None:
        expression = self.expression_var.get()
        try:
            result = ExpressionEvaluator.evaluate(expression)
        except Exception as error:
            self.result_var.set("Błąd")
            messagebox.showerror("Błąd", str(error))
            return

        if result.is_integer():
            display_result = str(int(result))
        else:
            display_result = str(result)

        self.result_var.set(display_result)
        self.expression_var.set(display_result)

    def run(self) -> None:
        self.window.mainloop()


def main() -> None:
    app = CalculatorApp()
    app.run()


if __name__ == "__main__":
    main()

