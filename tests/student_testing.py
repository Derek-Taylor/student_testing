def testDistance(studentFunction):
    print("----- ----- ----- ----- ----- ----- ----")
    print("Test Distance")
    print("----- ----- ----- ----- ----- ----- ----")
    distance = studentFunction
    arguments = ['x1','y1','x2','y2']
    tests = [([0, 1, 0, 1], 0),
             ([0, 0, 0, 0], 0),
            ([1, 0, 0, 0],1),
            ([0, 2, 0, 0], 2),
            ([1, 5, 1, 12], 7),
            ([0, 2, 3, 6], 5),
            ([-12,-10,-10,-10], 2),
            ([-12,10,10,-10], 29.7321374)
             ]
    score = 0
    testNum = 1
    for test in tests:
      # print("----- ----- ----- ----- ----- ----- ----")
      print(f"Test # {testNum}")
      passed = "FAIL"
      studentAns = distance(test[0][0],test[0][1],test[0][2],test[0][3])
      if studentAns == test[1] or abs(studentAns - test[1]) / test[1] < 0.001:
        score += 1
        passed = "PASS"
      if passed == "PASS":
        print(f"result {passed}")
      else:
        argString = ", ".join([arguments[i] + " = " + str(test[0][i]) for i in range(len(arguments))])
        print( f"result {passed}\narguments {argString}\nexpected {test[1]}\nstudent result {studentAns}")
      print("----- ----- ----- ----- ----- ----- ----")
      testNum += 1
    print("----- ----- ----- ----- ----- ----- ----")
    print(f"Final Results {score}/{len(tests)} tests passed")
    print("----- ----- ----- ----- ----- ----- ----")
