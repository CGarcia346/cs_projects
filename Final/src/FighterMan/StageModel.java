package FighterMan;

import java.util.ArrayList;
import java.util.Random;

/**
 * Model of the Stage and characters within it
 */
public class StageModel  {

    public enum CellValue {
        EMPTY, USER, ENEMY
    };
    private CellValue[][] cells;
    private ArrayList<Player> combatants= new ArrayList<Player>();
    private int turn = 0;

    private int level;
    private int userRow;
    private int userColumn;
    private int actionCredit;
    private int playerHP;
    private int enemyHP;

    private ArrayList[][] moveable;

    private boolean gameOver;

    public StageModel(int rowCount, int columnCount){
        assert rowCount > 0 && columnCount > 0;
        this.cells = new CellValue[rowCount][columnCount];
        this.startNewGame();
    }
    /**
     * Starts a game for the user
     */
    public void startNewGame(){
        this.gameOver = false;
        this.level = 1;
        this.initialize();
    }

    /**
     * Sets up the stage
     */
    private void initialize(){

        int rowCount = this.cells.length;
        int columnCount = this.cells[0].length;

        // Empty all the cells
        for (int row = 0; row < rowCount; row++) {
            for (int column = 0; column < columnCount; column++) {
                this.cells[row][column] = CellValue.EMPTY;
            }
        }

        // Place the runner
        Player user = new Player();
        this.actionCredit = 10;
        this.turn = 0;
        this.userRow = 5;
        this.userColumn = 3;
        this.cells[this.userRow][this.userColumn] = CellValue.USER;
        combatants.add(user);

        if(this.level == 1){
            Player enemy = new Player();
            this.cells[5][6] = CellValue.ENEMY;
            combatants.add(enemy);
        }
        else if(this.level == 2){
            this.cells[5][6] = CellValue.ENEMY;
            this.cells[4][6] = CellValue.ENEMY;
        }
        else if(this.level == 3){
            this.cells[5][6] = CellValue.ENEMY;
            this.cells[4][6] = CellValue.ENEMY;
            this.cells[6][6] = CellValue.ENEMY;
        }

    }

    private void boundaries(){

        //this.moveable = this.cells.length;
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
     * @param  rowChange
     * @param  columnChange
     */
    public void moveCharacter(int rowChange, int columnChange){
        if (this.gameOver || this.turn != 0 || this.actionCredit == 0) {
            if(this.actionCredit == 0){
                this.actionCredit = 10;
                this.turn++;
            }
            return;
        }

        int newRow = this.userRow + rowChange;
        if (newRow < 4) {
            newRow = 4;
        }
        if (newRow > 6) {
            newRow = 6;
        }

        int newColumn = this.userColumn + columnChange;
        if (newColumn < 2) {
            newColumn = 2;
        }
        if (newColumn > 4) {
            newColumn = 4;
        }


        this.cells[this.userRow][this.userColumn] = CellValue.EMPTY;
        this.userRow = newRow;
        this.userColumn = newColumn;
        this.cells[this.userRow][this.userColumn] = CellValue.USER;
        this.actionCredit--;
    }


    public boolean isGameOver(){
        return false;
    }

    public boolean complete(){
        return true;
    }

    public void replay(){

    }

    public void attack(){

    }
    public void spAttack(){

    }

    public int getRowCount() {
        return this.cells.length;
    }

    public int getColumnCount() {
        assert this.cells.length > 0;
        return this.cells[0].length;
    }

    public CellValue getCellValue(int row, int column) {
        assert row >= 0 && row < this.cells.length && column >= 0 && column < this.cells[0].length;
        return this.cells[row][column];
    }
}
