package FighterMan;

import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;

/**
 * A class that creates the view for the game
 */


public class View extends Group {

    public final static double CELL_WIDTH = 50.0;
    @FXML private int rowCount;
    @FXML private int columnCount;
    private ImageView[][] cellViews;
    private Image user;
    private Image enemy;
    private Image enemy_2;
    private Image enemy_3;

    /**
     * retrieves of our characters for our view
     */
    public View() {
        this.user = new Image(getClass().getResourceAsStream("/res/Boxer.png"));
        this.enemy = new Image(getClass().getResourceAsStream("/res/BoxerE.png"));
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
        }

    }
    /**
     * Updates graphical changes of stage
     */
    public void updateStage(StageModel model) {

        assert model.getRowCount() == this.rowCount && model.getColumnCount() == this.columnCount;
        for (int row = 0; row < this.rowCount; row++) {
            for (int column = 0; column < this.columnCount; column++) {
                StageModel.CellValue cellValue = model.getCellValue(row, column);
                if (cellValue == StageModel.CellValue.USER) {
                    this.cellViews[row][column].setImage(this.user);
                } else if (cellValue == StageModel.CellValue.ENEMY1) {
                    this.cellViews[row][column].setImage(this.enemy);
                } else {
                    this.cellViews[row][column].setImage(null);
                }
            }
        }
    }
    /**
     * Updates graphical changes of player
     */
    public void updateCharacters(){

    }
}
