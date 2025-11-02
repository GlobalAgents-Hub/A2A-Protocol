import argparse
import datetime
import ast
import operator
from typing import Any, Dict, Callable

#!/usr/bin/env python3
# teste.py
# Demo simples em Python: um "agent" interativo com comandos básicos.
# Uso:
#   python teste.py --repl        # modo interativo
#   python teste.py echo "olá"    # executa comando único
#   python teste.py math "2+3*4"  # avalia expressão segura


class DemoAgent:
    """Agente simples que executa comandos predefinidos."""

    def __init__(self) -> None:
        self.commands: Dict[str, Callable[[str], str]] = {
            "echo": self.cmd_echo,
            "time": self.cmd_time,
            "greet": self.cmd_greet,
            "math": self.cmd_math,
            "help": self.cmd_help,
        }

    def handle(self, command: str, payload: str = "") -> str:
        cmd = command.strip().lower()
        if cmd in self.commands:
            return self.commands[cmd](payload)
        return f"Comando desconhecido: {command!r}. Use 'help' para listar comandos."

    def cmd_echo(self, payload: str) -> str:
        return payload

    def cmd_time(self, payload: str) -> str:
        now = datetime.datetime.now()
        return now.isoformat(sep=" ", timespec="seconds")

    def cmd_greet(self, payload: str) -> str:
        name = payload.strip() or "amigo"
        return f"Olá, {name}!"

    def cmd_help(self, payload: str) -> str:
        keys = ", ".join(sorted(self.commands.keys()))
        return f"Comandos disponíveis: {keys}"

    def cmd_math(self, payload: str) -> str:
        """Avalia expressões aritméticas simples de forma segura usando AST."""
        expr = payload.strip()
        if not expr:
            return "Forneça uma expressão, ex: 2+3*4"
        try:
            value = eval_arithmetic(expr)
            return str(value)
        except Exception as e:
            return f"Erro ao avaliar expressão: {e}"


# --- função auxiliar para avaliar expressões aritméticas com segurança ---
_ALLOWED_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos, 
}


def eval_arithmetic(expr: str) -> Any:
    """
    Analisa e avalia expressões contendo números e operadores aritméticos básicos.
    Lança ValueError para nós AST não permitidos.
    """
    node = ast.parse(expr, mode="eval")

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        if isinstance(n, ast.Constant):  # Python 3.8+
            if isinstance(n.value, (int, float)):
                return n.value
            raise ValueError("Constante não numérica não permitida")
        if isinstance(n, ast.BinOp):
            op_type = type(n.op)
            if op_type not in _ALLOWED_OPS:
                raise ValueError(f"Operador não permitido: {op_type}")
            left = _eval(n.left)
            right = _eval(n.right)
            return _ALLOWED_OPS[op_type](left, right)
        if isinstance(n, ast.UnaryOp):
            op_type = type(n.op)
            if op_type not in _ALLOWED_OPS:
                raise ValueError(f"Operador unário não permitido: {op_type}")
            operand = _eval(n.operand)
            return _ALLOWED_OPS[op_type](operand)
        raise ValueError(f"Nó AST não permitido: {type(n)}")

    return _eval(node)


# --- CLI / REPL ---
def repl(agent: DemoAgent) -> None:
    print("DemoAgent REPL. Digite 'help' para comandos. 'exit' ou Ctrl-C para sair.")
    try:
        while True:
            line = input("> ").strip()
            if not line:
                continue
            if line.lower() in {"exit", "quit"}:
                print("Saindo.")
                break
            parts = line.split(" ", 1)
            cmd = parts[0]
            payload = parts[1] if len(parts) > 1 else ""
            result = agent.handle(cmd, payload)
            print(result)
    except (KeyboardInterrupt, EOFError):
        print("\nSaindo.")


def main():
    parser = argparse.ArgumentParser(description="DemoAgent - exemplo simples em Python")
    parser.add_argument("--repl", action="store_true", help="Entrar em modo interativo")
    parser.add_argument("command", nargs="?", help="Comando a executar (ex: echo, time, greet, math)")
    parser.add_argument("payload", nargs="?", help="Payload do comando (texto ou expressão)")
    args = parser.parse_args()

    agent = DemoAgent()

    if args.repl or args.command is None:
        repl(agent)
        return

    result = agent.handle(args.command, args.payload or "")
    print(result)


if __name__ == "__main__":
    main()