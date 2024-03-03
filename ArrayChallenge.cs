using System;
using System.Collections.Generic;

class MainClass {

  public static string ArrayChallenge(string[] strArr) {

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
        return distance.ToString();
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
      return "0";
    }
    // if (strArr == null || strArr.Length == 0 || strArr[0].Length == 0)
    //         return "0";

    //     int rows = strArr.Length;
    //     int cols = strArr[0].Length;

    //     int rowOne = -1;
    //     int colOne = -1;
        
    //     // Find the position of 1
    //     for (int i = 0; i < rows; i++) {
    //         for (int j = 0; j < cols; j++) {
    //             if (strArr[i][j] == '1') {
    //                 rowOne = i;
    //                 colOne = j;
    //                 break;
    //             }
    //         }
    //         if (rowOne != -1) break;
    //     }

    //     if (rowOne == -1 || colOne == -1) return "0";

    //     int minDistance = int.MaxValue;
        
    //     // Search for the nearest 2
    //     for (int i = 0; i < rows; i++) {
    //         for (int j = 0; j < cols; j++) {
    //             if (strArr[i][j] == '2') {
    //                 int distance = Math.Min(Math.Abs(i - rowOne), rows - Math.Abs(i - rowOne)) +
    //                                Math.Min(Math.Abs(j - colOne), cols - Math.Abs(j - colOne));
    //                 minDistance = Math.Min(minDistance, distance);
    //             }
    //         }
    //     }

    //     return minDistance == int.MaxValue ? "0" : minDistance.ToString();


  static void Main() {  

    // keep this function call here
    Console.WriteLine(ArrayChallenge(Console.ReadLine()));
    
  } 

}