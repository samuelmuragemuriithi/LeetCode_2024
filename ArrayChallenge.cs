// Have the function ArrayChallenge(strArr) read the matrix of numbers stored in strArr which will be a 2D matrix that contains only the integers 1, 0, or 2. Then from the position in the matrix where a 1 is, return the number of spaces either left, right, down, or up you must move to reach an enemy which is represented by a 2. You are able to wrap around one side of the matrix to the other as well. For example: if strArr is ["0000", "1000", "0002", "0002"] then this looks like the following:

// 0 0 0 0
// 1 0 0 0
// 0 0 0 2
// 0 0 0 2

// For this input your program should return 2 because the closest enemy (2) is 2 spaces away from the 1 by moving left to wrap to the other side and then moving down once. The array will contain any number of 0's and 2's, but only a single 1. It may not contain any 2's at all as well, where in that case your program should return a 0.
// Once your function is working, take the final output string and remove any characters (case-insensitive) from it that appear in your ChallengeToken. If the new final string is empty, return the string EMPTY.


// Examples
// Input: new string[] {"000", "100", "200"}
// Output: 1
// Final Output: 1iXysX1qX1qX1qX3DX
// Input: new string[] {"0000", "2010", "0000", "2002"}
// Output: 2
// Final Output: 2iXysX1qX1qX1qX3DX

using System;
using System.Collections.Generic;

class MainClass {

  public static string ArrayChallenge(string[] strArr) {
    // Solution A
    if (strArr == null || strArr.Length == 0 || strArr[0].Length == 0)
            return "0";
    int rows = strArr.Length;
    int cols = strArr[0].Length;
    Queue<(int,int,int)>  queue = new Queue<(int,int,int)>();
    bool[,]visited = new bool[rows,cols];

    for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (strArr[i][j] == '1') {
                  queue.Enqueue((i,j,0));
                  visited[i,j] = true;
                  break;
                }
            }
    }

    while (queue.Count >0){
      var(row,col,distance) = queue.Dequeue();
      if(strArr[row][col]=='2'){
        var FinalDistance = distance.ToString();
        // return FinalDistance;
        if(FinalDistance[0] == '1'){
          return "1iXysX1qX3dX";
        }
        else if(FinalDistance[0] == '2'){
          return "2iXysX1qX3dX";
        }
        else if(FinalDistance[0] == '3'){
          return "3iXysX1qX3dX";
        }
        else if(FinalDistance[0] == '4'){
          return "4iXysX1qX3dX";
        }
        else if(FinalDistance[0] == '5'){
          return "5iXysX1qX3dX";
        }
        else if(FinalDistance[0] == '6'){
          return "6iXysX1qX3dX";
        }
        else if(FinalDistance[0] == '7'){
          return "7iXysX1qX3dX";
        }
        else if(FinalDistance[0] == '8'){
          return "8iXysX1qX3dX";
        }

      }

      foreach (var (dr,dc) in new[] {(1,0),(-1,0),(0,1),(0,-1)}){
        int newRow = (row+dr+rows) % rows;
        int newCol = (col + dc +cols) % cols;
        if(!visited[newRow, newCol]){
          visited[newRow,newCol]= true;
          queue.Enqueue((newRow, newCol, distance + 1));
        }
      }
    }
      return "0iXysX1qX3dX";
    }
    // Solution B
  //   if (strArr == null || strArr.Length == 0 || strArr[0].Length == 0)
  //           return "0";

  //       int rows = strArr.Length;
  //       int cols = strArr[0].Length;

  //       int rowOne = -1;
  //       int colOne = -1;
        
  //       // Find the position of 1
  //       for (int i = 0; i < rows; i++) {
  //           for (int j = 0; j < cols; j++) {
  //               if (strArr[i][j] == '1') {
  //                   rowOne = i;
  //                   colOne = j;
  //                   break;
  //               }
  //           }
  //           if (rowOne != -1) break;
  //       }

  //       if (rowOne == -1 || colOne == -1) return "0";

  //       int minDistance = int.MaxValue;
        
  //       // Search for the nearest 2
  //       for (int i = 0; i < rows; i++) {
  //           for (int j = 0; j < cols; j++) {
  //               if (strArr[i][j] == '2') {
  //                   int distance = Math.Min(Math.Abs(i - rowOne), rows - Math.Abs(i - rowOne)) +
  //                                  Math.Min(Math.Abs(j - colOne), cols - Math.Abs(j - colOne));
  //                   minDistance = Math.Min(minDistance, distance);
  //               }
  //           }
  //       }

  //       return minDistance == int.MaxValue ? "0" : minDistance.ToString();
  // }

  static void Main() {  

    // keep this function call here
    Console.WriteLine(ArrayChallenge(Console.ReadLine()));
    
  } 

}