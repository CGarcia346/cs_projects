package FighterMan;

import java.util.ArrayList;
import java.util.Random;

/**
 * Model of the Stage and characters within it
 */
public class StageModel  {

    public enum CellValue {
        EMPTY, USER, ENEMY1, ENEMY2, ENEMY3
    };
    private CellValue[][] cells;
    private ArrayList<Player> combatants= new ArrayList<Player>();
    private int turn = 0;

    private int level;
    private int userRow;
    private int userColumn;
    private int actionCredit;

    private ArrayList[][] moveable;

    private boolean winner;
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
            this.cells[5][6] = CellValue.ENEMY1;
            combatants.add(enemy);
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
        int player = this.turn;
        Player attacker = this.combatants.get(player);
        int damage = attacker.attack();
        int range = attacker.getAttackRange();
        int receiver = this.userColumn + range;
        CellValue locationHit= getCellValue(this.userRow, receiver);
        if(locationHit == CellValue.ENEMY1){
            this.combatants.get(1).takeDamage(damage);
        }
        else if(locationHit == CellValue.ENEMY2){
            this.combatants.get(2).takeDamage(damage);
        }
        else if(locationHit == CellValue.ENEMY3){
            this.combatants.get(3).takeDamage(damage);
        }
    }

    public void spAttack(){

    }

    public boolean levelComplete(){
        boolean success = false;
        if(this.level == 1){
            if(this.combatants.get(1).isDead()){
                this.level++;
                success = true;
            }
        }

        else if(this.level == 2){
            if(this.combatants.get(1).isDead() && this.combatants.get(2).isDead()){
                this.level++;
                success = true;
            }
        }
        else if(this.level == 3){
            if(this.combatants.get(1).isDead() && this.combatants.get(2).isDead() && this.combatants.get(3).isDead()){
                success = true;
                winner = true;
            }
        }
        return success;
    }

    public void levelcontinue(){

        if(this.level == 2){
            this.cells[5][6] = CellValue.ENEMY1;
            this.cells[4][6] = CellValue.ENEMY2;
        }
        else if(this.level == 3){
            this.cells[5][6] = CellValue.ENEMY1;
            this.cells[4][6] = CellValue.ENEMY2;
            this.cells[6][6] = CellValue.ENEMY3;
        }
    }

    public boolean isWinner(){
        return this.winner;
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
    public int getPlayerHP(){
        return this.combatants.get(0).getHP();

    }
}
