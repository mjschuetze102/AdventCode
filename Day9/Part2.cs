using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode.Day9
{
    class Part2
    {
        private static HashSet<string> traveledTo = new HashSet<string>();

        private static Dictionary<string, int[]> moveMatrix = new Dictionary<string, int[]> {
            { "U", new int[] { -1,  0 } },
            { "D", new int[] {  1,  0 } },
            { "L", new int[] {  0, -1 } },
            { "R", new int[] {  0,  1 } },
        };

        static void Temp()
        {
            string[] lines = System.IO.File.ReadAllLines(@"C:\Users\User\Downloads\advent.txt");

            List<int[]> knots = Enumerable.Repeat(new int[] { 0, 0 }, 10).ToList();
            foreach (string line in lines)
            {
                string[] move = line.Split(" ");
                for (int i = 0; i < Int32.Parse(move[1]); i++)
                {
                    knots[0] = knots[0].Zip(moveMatrix[move[0]], (x, y) => x + y).ToArray();

                    for(int knot = 1; knot < knots.Count; knot++)
                    {
                        double distance = Math.Sqrt(Math.Pow(knots[knot - 1][0] - knots[knot][0], 2) + Math.Pow(knots[knot - 1][1] - knots[knot][1], 2));
                        if (distance > Math.Sqrt(2))
                        {
                            knots[knot] = knots[knot - 1].Zip(knots[knot], (x, y) => Math.Sign(x - y) + y).ToArray();
                        }
                    }
                    
                    traveledTo.Add(knots[^1][0] + ":" + knots[^1][1]);
                }
            }

            Console.WriteLine(traveledTo.Count);
        }
    }
}
