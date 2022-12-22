using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode.Day9
{
    class Part1
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

            int[] head = new int[] { 4, 0 };
            int[] tail = new int[] { 4, 0 };
            foreach (string line in lines)
            {
                string[] move = line.Split(" ");
                for (int i = 0; i < Int32.Parse(move[1]); i++)
                {
                    head = head.Zip(moveMatrix[move[0]], (x, y) => x + y).ToArray();

                    double distance = Math.Sqrt(Math.Pow(head[0] - tail[0], 2) + Math.Pow(head[1] - tail[1], 2));
                    if (distance > Math.Sqrt(2))
                    {
                        tail = head.Zip(tail, (x, y) => Math.Sign(x - y) + y).ToArray();
                    }

                    traveledTo.Add(tail[0] + ":" + tail[1]);
                }
            }

            Console.WriteLine(traveledTo.Count);
        }
    }
}
