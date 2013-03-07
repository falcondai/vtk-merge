#!/usr/bin/python

# Name: vtk-merge.py
# Author: Falcon Dai (me@falcondai.com)
# Description: This script merges two vtk files into one.

from vtk import vtkAppendPolyData, vtkPolyDataReader, vtkPolyDataWriter

def merge(pd1, pd2):
    """
    merge two PolyDataSets into one.

    @param vtkPolyData pd1  the first dataset
    @param vtkPolyData pd2  the second dataset
    
    @return vtkPolyData the merged dataset
    """
    a = vtkAppendPolyData()
    a.AddInput(pd1)
    a.AddInput(pd2)
    return a.GetOutput()

if __name__ == '__main__':
    import sys
    import os
    if len(sys.argv) < 4:
        print 'Need more inputs.'
        print 'Usage: ./vtk-merge.py in-vtk1 in-vtk2 out-vtk'
    else:
        fn1, fn2, of = sys.argv[1:4]
        if not os.access(fn1, os.R_OK) or not os.access(fn2, os.R_OK):
            print 'Cannot read in-vtk\'s'
        else:
            r1 = vtkPolyDataReader()
            r1.SetFileName(fn1)
            r2 = vtkPolyDataReader()
            r2.SetFileName(fn2)
            w = vtkPolyDataWriter()
            w.SetFileName(of)
            w.SetInput(merge(r1.GetOutput(), r2.GetOutput()))
            w.Write()
    
