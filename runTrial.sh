#!/bin/bash
echo "Start Trial"
echo ""

#=====Begin Steepest Descent Trials
echo "Begin Steepest Descent Trials"

echo "" > steepestDescentTrials
timeout 1s python steepestDescent.py 1.2 1.2 0.1 0.01 2.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 1.2 1.2 0.01 0.001 2.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 1.2 1.2 0.1 0.01 10.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 1.2 1.2 0.01 0.001 10.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 1.2 1.2 0.1 0.01 20.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 1.2 1.2 0.01 0.001 20.0 | xargs echo >> steepestDescentTrials
echo "." >> steepestDescentTrials
echo "1 done"

timeout 1s python steepestDescent.py -1.2 1.0 0.1 0.01 2.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py -1.2 1.0 0.01 0.001 2.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py -1.2 1.0 0.1 0.01 10.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py -1.2 1.0 0.1 0.01 10.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py -1.2 1.0 0.01 0.001 10.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py -1.2 1.0 0.1 0.01 20.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py -1.2 1.0 0.01 0.001 20.0 | xargs echo >> steepestDescentTrials
echo "." >> steepestDescentTrials
echo "2 done"

timeout 1s python steepestDescent.py 10.0 0.0 0.1 0.01 2.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 10.0 0.0 0.01 0.001 2.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 10.0 0.0 0.1 0.01 10.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 10.0 0.0 0.01 0.001 10.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 10.0 0.0 0.1 0.01 20.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 10.0 0.0 0.01 0.001 20.0 | xargs echo >> steepestDescentTrials
echo "." >> steepestDescentTrials
echo "3 done"

timeout 1s python steepestDescent.py 1.5 15.0 0.1 0.01 2.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 1.5 15.0 0.01 0.001 2.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 1.5 15.0 0.1 0.01 10.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 1.5 15.0 0.01 0.001 10.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 1.5 15.0 0.1 0.01 20.0 | xargs echo >> steepestDescentTrials
timeout 1s python steepestDescent.py 1.5 15.0 0.01 0.001 20.0 | xargs echo >> steepestDescentTrials

echo "." >> steepestDescentTrials
echo "4 done"

#=====Begin Fletcher-Reeves Trials
echo "Begin Fletcher-Reeves Trials"

echo "" > fletcherReevesTrials
timeout 1s python fletcherReeves.py 1.2 1.2 0.1 0.01 2.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 1.2 1.2 0.01 0.001 2.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 1.2 1.2 0.1 0.01 10.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 1.2 1.2 0.01 0.001 10.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 1.2 1.2 0.1 0.01 20.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 1.2 1.2 0.01 0.001 20.0 | xargs echo >> fletcherReevesTrials
echo "." >> fletcherReevesTrials
echo "1 done"

timeout 1s python fletcherReeves.py -1.2 1.0 0.1 0.01 2.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py -1.2 1.0 0.01 0.001 2.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py -1.2 1.0 0.1 0.01 10.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py -1.2 1.0 0.01 0.001 10.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py -1.2 1.0 0.1 0.01 20.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py -1.2 1.0 0.01 0.001 20.0 | xargs echo >> fletcherReevesTrials
echo "." >> fletcherReevesTrials
echo "2 done"

timeout 1s python fletcherReeves.py 10.0 0.0 0.1 0.01 2.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 10.0 0.0 0.01 0.001 2.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 10.0 0.0 0.1 0.01 10.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 10.0 0.0 0.01 0.001 10.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 10.0 0.0 0.1 0.01 20.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 10.0 0.0 0.01 0.001 20.0 | xargs echo >> fletcherReevesTrials
echo "." >> fletcherReevesTrials
echo "3 done"

timeout 1s python fletcherReeves.py 1.5 15.0 0.1 0.01 2.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 1.5 15.0 0.01 0.001 2.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 1.5 15.0 0.1 0.01 10.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 1.5 15.0 0.01 0.001 10.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 1.5 15.0 0.1 0.01 20.0 | xargs echo >> fletcherReevesTrials
timeout 1s python fletcherReeves.py 1.5 15.0 0.01 0.001 20.0 | xargs echo >> fletcherReevesTrials
echo "." >> fletcherReevesTrials
echo "4 done"

echo ""
echo "End Trials"
