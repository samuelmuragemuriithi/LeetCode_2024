using System;
using System.Linq;

class MainClass {

  public static int MathChallenge(int num) {
    // Define OCG - Math Challenge
    var varOcg = num;
    string numString = num.ToString();
    char[] charArray = numString.ToCharArray();

    int i, j;

    // Find the largest index i such that charArray[i] < charArray[i+1]
    for (i = charArray.Length - 2; i >= 0; i--) {
      if (charArray[i] < charArray[i + 1]) {
        break;
      }
    }

    // If no such index exists, then the input number is the largest permutation
    if (i == -1) {
      return -1;
    }

    // Find the largest index j greater than i such that charArray[i] < charArray[j]
    for (j = charArray.Length - 1; j > i; j--) {
      if (charArray[j] > charArray[i]) {
        break;
      }
    }

    // Swap charArray[i] and charArray[j]
    char temp = charArray[i];
    charArray[i] = charArray[j];
    charArray[j] = temp;

    // Reverse the substring from i+1 to the end of the string
    Array.Reverse(charArray, i + 1, charArray.Length - i - 1);

    // Convert the char array back to an integer
    int nextPermutation = Convert.ToInt32(new string(charArray));

    // Remove characters from ChallengeToken
    string ChallengeToken = "6moz905l47";
    string finalOutput = new string(nextPermutation.ToString().Where(c => !ChallengeToken.Contains(char.ToLower(c))).ToArray());

    // If the new final string is empty, return "EMPTY"
    if (string.IsNullOrEmpty(finalOutput))
      return -1;

    return Convert.ToInt32(finalOutput);
  }

  static void Main() {
    // keep this function call here
    Console.WriteLine(MathChallenge(Convert.ToInt32(Console.ReadLine())));
  }
}
