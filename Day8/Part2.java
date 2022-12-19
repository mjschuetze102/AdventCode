import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class Part2 {

    private static class Tree {

        private final int height;
        private int score = 0;

        public Tree(String height) {
            this.height = Integer.parseInt(height);
        }

        public int getHeight() {
            return height;
        }

        public int getScore() {
            return score;
        }

        public void setScore(int score) {
            this.score = score;
        }
    }

    public static void main(String[] args) throws IOException {
        String file = "C:\\Users\\User\\Downloads\\advent.txt";

        ArrayList<List<Tree>> forest = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            for(String line; (line = reader.readLine()) != null; ) {
                List<String> chars = Arrays.asList(line.split(""));
                forest.add(chars.stream().map(Tree::new).collect(Collectors.toList()));
            }
        }

        for (int row = 0; row < forest.size(); row++) {
            for (int col = 0; col < forest.get(0).size(); col++) {
                Tree tree = forest.get(row).get(col);

                int top = 0;
                for (int distance = 1; distance <= row; distance++) {
                    top++;
                    if (forest.get(row - distance).get(col).getHeight() >= tree.getHeight()) {
                        break;
                    }
                }

                int left = 0;
                for (int distance = 1; distance <= col; distance++) {
                    left++;
                    if (forest.get(row).get(col - distance).getHeight() >= tree.getHeight()) {
                        break;
                    }
                }

                int bot = 0;
                for (int distance = 1; distance < forest.size() - row; distance++) {
                    bot++;
                    if (forest.get(row + distance).get(col).getHeight() >= tree.getHeight()) {
                        break;
                    }
                }

                int right = 0;
                for (int distance = 1; distance < forest.get(0).size() - col; distance++) {
                    right++;
                    if (forest.get(row).get(col + distance).getHeight() >= tree.getHeight()) {
                        break;
                    }
                }

                tree.setScore(top * left * right * bot);
            }
        }

        System.out.println(Collections.max(forest.stream()
                .flatMap(Collection::stream)
                .map(Tree::getScore)
                .collect(Collectors.toList())));
    }
}
