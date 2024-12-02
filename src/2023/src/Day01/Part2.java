package Day1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Part2 {

    enum Numbers {
        zero,
        one,
        two,
        three,
        four,
        five,
        six,
        seven,
        eight,
        nine
    }

    static String numbers = "0123456789";

    static int indexOf(String line, String num) {
        int index = line.indexOf(num);
        if (index < 0) {
            return Integer.MAX_VALUE;
        }

        return index;
    }

    static String convertToInt(String num) {
        try {
            Integer.parseInt(num);
            return num;
        } catch (NumberFormatException e) {
            return "" + Numbers.valueOf(num).ordinal();
        }
    }

    public static void main(String[] args) throws IOException {
        String file = "C:\\Users\\User\\Downloads\\advent.txt";

        int total = 0;
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            for(String line; (line = reader.readLine()) != null; ) {
                List<String> numStrings = Stream.concat(
                        Arrays.stream(Numbers.values()).map(Enum::toString),
                        Arrays.stream(numbers.split(""))
                ).collect(Collectors.toList());

                final String temp = line;
                String firstDigit = numStrings.stream()
                        .reduce((num1, num2) -> indexOf(temp, num1) < indexOf(temp, num2) ? num1 : num2)
                        .orElseThrow(RuntimeException::new);

                String secondDigit = numStrings.stream()
                        .reduce((num1, num2) -> temp.lastIndexOf(num1) > temp.lastIndexOf(num2) ? num1 : num2)
                        .orElseThrow(RuntimeException::new);

                total += Integer.parseInt(convertToInt(firstDigit) + convertToInt(secondDigit));
            }
        }

        System.out.println(total);
    }
}
