package FighterMan;

import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;

/**
 * A class that creates the view for the game
 */


public class View extends Group {
    public final static double CELL_WIDTH = 20.0;

    @FXML private int rowCount;
    @FXML private int columnCount;
    private ImageView[][] cellViews;
    private Image user;

    /**
     * retrieves of our characters for our view
     */
    public View() {
        this.user = new Image(getClass().getResourceAsStream("/res/Boxer.png"));
    }
    public int getRowCount() {
        return this.rowCount;
    }
    public void setRowCount(int rowCount) {
        this.rowCount = rowCount;
        this.initializeGrid();
    }
    public int getColumnCount() {
        return this.columnCount;
    }
    public void setColumnCount(int columnCount) {
        this.columnCount = columnCount;
        this.initializeGrid();
    }
    /**
     * initializes player sprite and starting location
     */
    private void initializePlayer() {
        this.cellViews[13][10].setImage(this.user);
    }
    /**
     * initializes stage graphic
     */
    private void initializeGrid() {
        if (this.rowCount > 0 && this.columnCount > 0) {
            this.cellViews = new ImageView[this.rowCount][this.columnCount];
            for (int row = 0; row < this.rowCount; row++) {
                for (int column = 0; column < this.columnCount; column++) {
                    ImageView imageView = new ImageView();
                    imageView.setX((double)column * CELL_WIDTH);
                    imageView.setY((double)row * CELL_WIDTH);
                    imageView.setFitWidth(CELL_WIDTH);
                    imageView.setFitHeight(CELL_WIDTH);
                    this.cellViews[row][column] = imageView;
                    this.getChildren().add(imageView);

                }
            }
            initializePlayer();
        }

    }
    /**
     * Updates graphical changes of stage
     */
    public void updateStage(StageModel model) {

    }
    /**
     * Updates graphical changes of player
     */
    public void updateCharacters(Player model){
    }
}
