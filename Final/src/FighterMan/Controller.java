package FighterMan;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import java.util.*;

public class Controller implements EventHandler<KeyEvent> {

    @FXML private View view;
    @FXML private ImageView boardImageView;
    private StageModel stageModel;

    public Controller(){

    }
    
    public void initialize() {
        this.stageModel = new StageModel(this.view.getRowCount(), this.view.getColumnCount());
        this.boardImageView.setFitWidth(this.view.getLayoutBounds().getWidth());
        this.boardImageView.setFitHeight(this.view.getLayoutBounds().getHeight());
        this.update();
    }

    public double getBoardWidth() {
        return view.CELL_WIDTH * this.view.getColumnCount();
    }

    public double getBoardHeight() {
        return view.CELL_WIDTH * this.view.getRowCount();
    }

    @Override
    public void handle(KeyEvent keyEvent) {
        boolean keyRecognized = true;
        KeyCode code = keyEvent.getCode();
        if (code == KeyCode.LEFT || code == KeyCode.A) {
            this.stageModel.moveCharacter(0, -1);
        } else if (code == KeyCode.RIGHT || code == KeyCode.D) {
            this.stageModel.moveCharacter(0, 1);
        } else if (code == KeyCode.UP || code == KeyCode.W) {
            this.stageModel.moveCharacter(-1, 0);
        } else if (code == KeyCode.DOWN || code == KeyCode.S) {
            this.stageModel.moveCharacter(1, 0);
        } else if (code == KeyCode.E){
            this.stageModel.attack();
        } else if (code == KeyCode.F){
            this.stageModel.spAttack();
        } else if (code == KeyCode.R) {
            if (this.stageModel.isGameOver()) {
                this.stageModel.startNewGame();
            }
        } else if (code == KeyCode.L) {
            if (this.stageModel.complete()) {
                this.stageModel.replay();
            }
        }
        else if (code == KeyCode.G) {
                this.stageModel.startNewGame();
        } else {
            keyRecognized = false;
        }

        if (keyRecognized) {
            this.update();
            keyEvent.consume();
        }
    }

    private void update(){
        this.view.updateStage(this.stageModel);
    }
}
