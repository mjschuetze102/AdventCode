import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Part1 {

    private static final int[][] pointsMatrix = { {3, 6, 0},
                                                  {0, 3, 6},
                                                  {6, 0, 3} };

    public static void main(String[] args) throws IOException {
        String file = "C:\\Users\\User\\Downloads\\advent.txt";

        int score = 0;
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            for(String line; (line = reader.readLine()) != null; ) {
                String[] moves = line.split(" ");

                int opponent = moves[0].charAt(0) - 'A';
                int player = moves[1].charAt(0) - 'X';

                score += (player + 1) + pointsMatrix[opponent][player];
            }
        }

        System.out.println("Score: " + score);
    }
}
