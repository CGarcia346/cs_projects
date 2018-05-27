package sample;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

public class Controller {

    @FXML private View View;
    private StageModel StageModel;

    public Controller(){

    }
    
    public void initialize() {
        this.StageModel = new StageModel(this.View.getRowCount(), this.View.getColumnCount());
        this.update();
    }

    public double getBoardWidth() {
        return View.CELL_WIDTH * this.View.getColumnCount();
    }

    public double getBoardHeight() {
        return View.CELL_WIDTH * this.View.getRowCount();
    }

    @Override
    public void handle(KeyEvent keyEvent) {
        boolean keyRecognized = true;
        KeyCode code = keyEvent.getCode();
        if (code == KeyCode.LEFT || code == KeyCode.A) {
            this.StageModel.moveCharacter(0, -1);
        } else if (code == KeyCode.RIGHT || code == KeyCode.D) {
            this.StageModel.moveCharacter(0, 1);
        } else if (code == KeyCode.UP || code == KeyCode.W) {
            this.StageModel.moveCharacter(-1, 0);
        } else if (code == KeyCode.DOWN || code == KeyCode.X) {
            this.StageModel.moveCharacter(1, 0);
        } else if (code == KeyCode.Q) {
            this.StageModel.moveCharacter(-1, -1);
        } else if (code == KeyCode.E) {
            this.StageModel.moveCharacter(-1, 1);
        } else if (code == KeyCode.Z) {
            this.StageModel.moveCharacter(1, -1);
        } else if (code == KeyCode.C) {
            this.StageModel.moveCharacter(1, 1);
        } else if (code == KeyCode.S) {
            this.StageModel.moveCharacter(0, 0);
        } else if (code == KeyCode.G) {
            if (this.StageModel.isGameOver()) {
                this.StageModel.startNewGame();
            }
        } else if (code == KeyCode.L) {
            if (this.StageModel.complete()) {
                this.StageModel.replay();
            }
        } else {
            keyRecognized = false;
        }

        if (keyRecognized) {
            this.update();
            keyEvent.consume();
        }
    }

    private void update(){

    }
}
