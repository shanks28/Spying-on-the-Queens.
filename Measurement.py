import Hill_Climbing
import psutil
import math
if(__name__=="__main__"):
    process=psutil.Process()
    start=process.memory_info().rss
    board=Hill_Climbing.simple_hill_climbing(10000,10000)
    stop=process.memory_info().rss
    print(stop-start)
    print("In MB :{}".format((stop-start)/(1024*1024)))
    print(Hill_Climbing.h_cost(board))