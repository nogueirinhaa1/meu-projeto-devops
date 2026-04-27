# tests/test_basic.py
import os
import py_compile

def test_app_compiles():
    """Verifica se app.py compila sem erros de sintaxe."""
    path = os.path.join(os.path.dirname(__file__), "..", "app.py")
    path = os.path.abspath(path)
    assert os.path.exists(path), "Arquivo app.py não encontrado"
    py_compile.compile(path, doraise=True)

def test_requirements_non_empty():
    """Verifica se requirements.txt existe e não está vazio."""
    req = os.path.join(os.path.dirname(__file__), "..", "requirements.txt")
    req = os.path.abspath(req)
    assert os.path.exists(req), "requirements.txt não encontrado"
    with open(req, "r", encoding="utf8") as f:
        lines = [l.strip() for l in f if l.strip()]
    assert len(lines) >= 1, "requirements.txt está vazio"

def test_dockerfile_has_from():
    """Verifica se Dockerfile existe e contém a instrução FROM."""
    df = os.path.join(os.path.dirname(__file__), "..", "Dockerfile")
    df = os.path.abspath(df)
    assert os.path.exists(df), "Dockerfile não encontrado"
    with open(df, "r", encoding="utf8") as f:
        content = f.read().upper()
    assert "FROM" in content, "Dockerfile parece inválido (sem FROM)"

def test_readme_exists():
    """Verifica se README.md existe (comprovante de repositório documentado)."""
    readme = os.path.join(os.path.dirname(__file__), "..", "README.md")
    readme = os.path.abspath(readme)
    assert os.path.exists(readme), "README.md não encontrado"

def test_app_has_main_guard_or_app_var():
    """Verifica se app.py tem guard 'if __name__' ou variável 'app' (indicador de app executável)."""
    path = os.path.join(os.path.dirname(__file__), "..", "app.py")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf8") as f:
        content = f.read()
    assert ("if __name__" in content) or ("app =" in content) or ("def main(" in content), \
        "app.py não contém guard 'if __name__', nem 'app =' nem 'def main(' — ajuste o teste se necessário"
