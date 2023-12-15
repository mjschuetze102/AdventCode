using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode.Day1
{
    class Part2
    {
        static void Temp()
        {
            string[] lines = System.IO.File.ReadAllLines(@"C:\Users\User\Downloads\advent.txt");

            int currCalories = 0;
            List<int> mostCalories = new List<int>() { 0, 0, 0 };

            foreach (string line in lines)
            {
                if (line == "")
                {
                    if (currCalories > mostCalories[0])
                    {
                        mostCalories.RemoveAt(0);

                        for (int index = 0; index < mostCalories.Count; index++)
                        {
                            if (currCalories < mostCalories[index])
                            {
                                mostCalories.Insert(index, currCalories);
                                break;
                            }
                        }

                        if (mostCalories.Count != 3) mostCalories.Add(currCalories);
                    }

                    currCalories = 0;
                    continue;
                }

                currCalories += Int32.Parse(line);
            }

            if (currCalories > mostCalories[0])
            {
                mostCalories.RemoveAt(0);
                mostCalories.Add(currCalories);
            }

            Console.WriteLine($"Calories: {mostCalories.Sum()}");
        }
    }
}
