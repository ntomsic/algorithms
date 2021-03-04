from pylint import epylint as lint

(pylint_stdout, pylint_stderr) = lint.py_run('algorithms', return_std=True)
pylint_output = pylint_stdout.read()

print(pylint_output)