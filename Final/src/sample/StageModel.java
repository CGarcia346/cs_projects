package sample;

import java.util.ArrayList;
import java.util.Random;

/**
 * Model of the Stage and characters within it
 */
public class StageModel  {

    private int playerHP;
    private int enemyHP;
    private ArrayList[][] moveable;
    private boolean gameOver;

    public StageModel(int row, int column){

    }
    /**
     * Starts a game for the user
     */
    public void startNewGame(){

    }

    /**
     * retrieves the positions of the Characters
     * @param  character
     * @return position of the characters
     */
    public void getCharacterPos(Player character){

    }
    /**
     * Will update the HP bar for a character/player that has taken damage
     * @param  HP
     * @param  character
     * @return an update to a character's HP bar
     */
    public void updateHPBar(int HP, Player character){

    }
    /**
     * Moves a character to a different position
     * @param  row
     * @param  column
     */
    public void moveCharacter(int row, int column){
    }

    /**
     * Sets up the stage
     */
    private void initialize(){

    }

    public boolean isGameOver(){

    }

    public boolean complete(){

    }

    public void replay(){

    }
}
