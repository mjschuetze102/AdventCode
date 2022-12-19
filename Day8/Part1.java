import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class Part1 {

    private static class Tree {

        private final int height;
        private boolean visible = false;

        public Tree(String height) {
            this.height = Integer.parseInt(height);
        }

        public int getHeight() {
            return height;
        }

        public boolean getVisible() {
            return visible;
        }

        public void setVisible(boolean visible) {
            this.visible = visible;
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
            int fromLeft = -1;
            int fromRight = -1;

            for (int col = 0; col < forest.get(0).size(); col++) {
                Tree leftTree = forest.get(row).get(col);
                if (leftTree.getHeight() > fromLeft) {
                    leftTree.setVisible(true);
                    fromLeft = leftTree.getHeight();
                }

                Tree rightTree = forest.get(row).get(forest.get(0).size() - 1 - col);
                if (rightTree.getHeight() > fromRight) {
                    rightTree.setVisible(true);
                    fromRight = rightTree.getHeight();
                }
            }
        }

        for (int col = 0; col < forest.get(0).size(); col++) {
            int fromTop = -1;
            int fromBot = -1;

            for (int row = 0; row < forest.size(); row++) {
                Tree topTree = forest.get(row).get(col);
                if (topTree.getHeight() > fromTop) {
                    topTree.setVisible(true);
                    fromTop = topTree.getHeight();
                }

                Tree botTree = forest.get(forest.size() - 1 - row).get(col);
                if (botTree.getHeight() > fromBot) {
                    botTree.setVisible(true);
                    fromBot = botTree.getHeight();
                }
            }
        }

        System.out.println(forest.stream()
                .flatMap(Collection::stream)
                .filter(Tree::getVisible)
                .count());
    }
}
