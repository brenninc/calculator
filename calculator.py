import parser
import sys

command = " ".join(sys.argv[1:])
st = parser.expr(command)
code = st.compile('file.py')
print command,"=",eval(code)

