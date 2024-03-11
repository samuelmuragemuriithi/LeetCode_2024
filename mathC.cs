using System;

class MainClass {

  public static int MathChallenge(int num) {
    // Define OCG - Math Challenge
    var varOcg = num;

    // Convert the number to an array of digits
    int[] digits = GetDigits(num);

    // Find the largest index i such that digits[i] < digits[i+1]
    int i;
    for (i = digits.Length - 2; i >= 0; i--) {
      if (digits[i] < digits[i + 1]) {
        break;
      }
    }

    // If no such index exists, then the input number is the largest permutation
    if (i == -1) {
      return -1;
    }

    // Find the largest index j greater than i such that digits[i] < digits[j]
    int j;
    for (j = digits.Length - 1; j > i; j--) {
      if (digits[j] > digits[i]) {
        break;
      }
    }

    // Swap digits[i] and digits[j]
    int temp = digits[i];
    digits[i] = digits[j];
    digits[j] = temp;

    // Reverse the subarray from i+1 to the end of the array
    Array.Reverse(digits, i + 1, digits.Length - i - 1);

    // Convert the array of digits back to an integer
    int nextPermutation = GetNumber(digits);

    // Remove characters from ChallengeToken
    string ChallengeToken = "6moz905l47";
    string finalOutput = RemoveCharacters(nextPermutation.ToString(), ChallengeToken);

    // If the new final string is empty, return -1
    if (string.IsNullOrEmpty(finalOutput))
      return -1;

    return Convert.ToInt32(finalOutput);
  }

  // Helper function to convert a number to an array of its digits
  private static int[] GetDigits(int num) {
    int numLength = (int)Math.Floor(Math.Log10(num)) + 1;
    int[] digits = new int[numLength];
    for (int i = numLength - 1; i >= 0; i--) {
      digits[i] = num % 10;
      num /= 10;
    }
    return digits;
  }

  // Helper function to convert an array of digits to a number
  private static int GetNumber(int[] digits) {
    int num = 0;
    foreach (int digit in digits) {
      num = num * 10 + digit;
    }
    return num;
  }

  // Helper function to remove characters from a string
  private static string RemoveCharacters(string input, string charactersToRemove) {
    foreach (char c in charactersToRemove.ToLower()) {
      input = input.Replace(char.ToLower(c).ToString(), "");
    }
    return input;
  }

  static void Main() {
    // keep this function call here
    Console.WriteLine(MathChallenge(Convert.ToInt32(Console.ReadLine())));
  }
}
