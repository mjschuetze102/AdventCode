import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Part2 {

    private static final int[][] moveMatrix = { {2, 0, 1},
                                                {0, 1, 2},
                                                {1, 2, 0} };

    public static void main(String[] args) throws IOException {
        String file = "C:\\Users\\User\\Downloads\\advent.txt";

        int score = 0;
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            for(String line; (line = reader.readLine()) != null; ) {
                String[] moves = line.split(" ");

                int opponent = moves[0].charAt(0) - 'A';
                int player = moves[1].charAt(0) - 'X';

                score += (player * 3) + (moveMatrix[opponent][player] + 1);
            }
        }

        System.out.println("Score: " + score);
    }
}
