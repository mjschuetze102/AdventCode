import javafx.util.Pair;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Part1 {

    public static void main(String[] args) throws IOException {
        String file = "C:\\Users\\User\\Downloads\\advent.txt";

        int count = 0;
        List<Pair<Integer, Integer>> elves = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            for(String line; (line = reader.readLine()) != null; ) {
                String[] assignments = line.split(",");

                for(String section: assignments) {
                    String[] parts = section.split("-");
                    Pair<Integer, Integer> range = new Pair<>(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]));

                    elves.add(range);
                }

                if (
                    (elves.get(0).getKey() <= elves.get(1).getKey() && elves.get(0).getValue() >= elves.get(1).getValue()) ||
                    (elves.get(0).getKey() >= elves.get(1).getKey() && elves.get(0).getValue() <= elves.get(1).getValue())
                )   count++;

                elves.clear();
            }
        }

        System.out.println(count);
    }
}
