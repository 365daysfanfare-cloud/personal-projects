#!/usr/bin/env python3
"""
Advanced Interactive Calculator
多機能な対話的計算機プログラム
"""

import math
import re
from typing import Union, List, Tuple


class Calculator:
    """高度な機能を備えた計算機クラス"""
    
    def __init__(self):
        self.history: List[Tuple[str, Union[int, float]]] = []
        self.variables: dict = {}
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """足し算"""
        return a + b
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """引き算"""
        return a - b
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """掛け算"""
        return a * b
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """割り算（ゼロ除算チェック付き）"""
        if b == 0:
            raise ValueError("ゼロで割ることはできません")
        return a / b
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """べき乗"""
        return base ** exponent
    
    def square_root(self, a: Union[int, float]) -> float:
        """平方根"""
        if a < 0:
            raise ValueError("負の数の平方根は計算できません")
        return math.sqrt(a)
    
    def factorial(self, n: int) -> int:
        """階乗"""
        if n < 0:
            raise ValueError("負の数の階乗は計算できません")
        if not isinstance(n, int):
            raise ValueError("階乗は整数でのみ計算できます")
        return math.factorial(n)
    
    def sine(self, angle_degrees: Union[int, float]) -> float:
        """サイン（度数法）"""
        radians = math.radians(angle_degrees)
        return math.sin(radians)
    
    def cosine(self, angle_degrees: Union[int, float]) -> float:
        """コサイン（度数法）"""
        radians = math.radians(angle_degrees)
        return math.cos(radians)
    
    def tangent(self, angle_degrees: Union[int, float]) -> float:
        """タンジェント（度数法）"""
        radians = math.radians(angle_degrees)
        return math.tan(radians)
    
    def logarithm(self, a: Union[int, float], base: Union[int, float] = 10) -> float:
        """対数"""
        if a <= 0:
            raise ValueError("対数の真数は正の数である必要があります")
        if base <= 0 or base == 1:
            raise ValueError("対数の底は1より大きい正の数である必要があります")
        return math.log(a, base)
    
    def modulo(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """剰余"""
        if b == 0:
            raise ValueError("ゼロで割ることはできません")
        return a % b
    
    def absolute_value(self, a: Union[int, float]) -> Union[int, float]:
        """絶対値"""
        return abs(a)
    
    def evaluate_expression(self, expression: str) -> Union[int, float]:
        """
        数式を評価する
        変数も使用可能（例：x + 5）
        """
        try:
            # 変数を置き換え
            eval_expr = expression
            for var, value in self.variables.items():
                eval_expr = re.sub(rf'\b{var}\b', str(value), eval_expr)
            
            # 安全な評価
            result = eval(eval_expr, {"__builtins__": {}}, 
                         {"sqrt": math.sqrt, "sin": self.sine, "cos": self.cosine,
                          "tan": self.tangent, "log": self.logarithm, "abs": abs,
                          "pi": math.pi, "e": math.e})
            return result
        except Exception as e:
            raise ValueError(f"数式の評価エラー: {str(e)}")
    
    def add_to_history(self, expression: str, result: Union[int, float]):
        """履歴に追加"""
        self.history.append((expression, result))
    
    def show_history(self):
        """計算履歴を表示"""
        if not self.history:
            print("履歴がありません")
            return
        
        print("\n=== 計算履歴 ===")
        for i, (expr, result) in enumerate(self.history, 1):
            print(f"{i}. {expr} = {result}")
        print()
    
    def set_variable(self, var_name: str, value: Union[int, float]):
        """変数を設定"""
        self.variables[var_name] = value
    
    def show_variables(self):
        """設定された変数を表示"""
        if not self.variables:
            print("変数が設定されていません")
            return
        
        print("\n=== 設定された変数 ===")
        for var, value in self.variables.items():
            print(f"{var} = {value}")
        print()


def print_menu():
    """メニューを表示"""
    print("\n" + "="*50)
    print("         高度な対話的計算機")
    print("="*50)
    print("基本操作:")
    print("  + - * / **     : 四則演算とべき乗")
    print("  %              : 剰余")
    print("  abs(x)         : 絶対値")
    print("  sqrt(x)        : 平方根")
    print("  factorial(x)   : 階乗")
    print("  sin/cos/tan(x) : 三角関数（度数法）")
    print("  log(x, base)   : 対数")
    print("\nコマンド:")
    print("  history        : 計算履歴を表示")
    print("  var            : 変数を表示")
    print("  set VAR VALUE  : 変数を設定（例：set x 5）")
    print("  clear          : 履歴をクリア")
    print("  help           : このメニューを表示")
    print("  exit/quit      : 終了")
    print("="*50 + "\n")


def main():
    """メイン処理"""
    calc = Calculator()
    print_menu()
    
    while True:
        try:
            user_input = input(">>> ").strip()
            
            if not user_input:
                continue
            
            # コマンド処理
            if user_input.lower() == 'exit' or user_input.lower() == 'quit':
                print("計算機を終了します。さようなら！")
                break
            
            elif user_input.lower() == 'help':
                print_menu()
            
            elif user_input.lower() == 'history':
                calc.show_history()
            
            elif user_input.lower() == 'var':
                calc.show_variables()
            
            elif user_input.lower().startswith('clear'):
                calc.history.clear()
                print("履歴をクリアしました")
            
            elif user_input.lower().startswith('set '):
                parts = user_input.split(maxsplit=2)
                if len(parts) == 3:
                    var_name = parts[1]
                    try:
                        value = float(parts[2])
                        calc.set_variable(var_name, value)
                        print(f"変数を設定しました: {var_name} = {value}")
                    except ValueError:
                        print("エラー: 値は数値である必要があります")
                else:
                    print("使用法: set 変数名 値")
            
            else:
                # 数式として評価
                result = calc.evaluate_expression(user_input)
                calc.add_to_history(user_input, result)
                print(f"= {result}")
        
        except ValueError as e:
            print(f"エラー: {e}")
        except KeyboardInterrupt:
            print("\n\n計算機を終了します。さようなら！")
            break
        except Exception as e:
            print(f"予期しないエラー: {e}")


if __name__ == "__main__":
    main()
