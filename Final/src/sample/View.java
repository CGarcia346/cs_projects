package sample;

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

    /**
     * retrieves of our characters for our view
     */
    public View() {
    }
    public int getRowCount() {
        return this.getRowCount();
    }
    public void setRowCount(int rowCount) {
        this.rowCount = rowCount;
    }
    public int getColumnCount() {
        return this.columnCount;
    }
    public void setColumnCount(int columnCount) {
        this.columnCount = rowCount;
    }
    /**
     * initializes player sprite and starting location
     */
    private void initializerPlayer() {

    }
    /**
     * initializes stage graphic
     */
    private void initializerGrid() {
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
