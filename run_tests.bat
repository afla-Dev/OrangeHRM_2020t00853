@echo off
pytest testCases/test_login.py testCases/test_leave.py -v --html=Reports/report.html --self-contained-html
pause