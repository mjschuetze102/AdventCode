package Day1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Part1 {

    public static void main(String[] args) throws IOException {
        String file = "C:\\Users\\User\\Downloads\\advent.txt";

        int total = 0;
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            for(String line; (line = reader.readLine()) != null; ) {
                line = line.replaceAll("[^0-9]+", "");

                total += Integer.parseInt("" + line.charAt(0) + line.charAt(line.length() - 1));
            }
        }

        System.out.println(total);
    }
}
