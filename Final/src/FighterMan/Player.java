package FighterMan;

import java.util.*;
import java.util.Random;
/**
 * A player/character that will perform actions on the stage
 */
public class Player implements PlayerInterface{

    private int HP  = 100;
    private int row = 6;
    private int column = 8;
    private boolean dead;

    public int get_row(){
        return this.row;
    }

    public int get_column(){
        return this.column;
    }
    /**
     * Moves a character to a position
     * @param  row
     * @param  column
     */

    public void move(int row, int column){

    }
    /**
     * A character's attack
     */
    public int attack(){
        return 25;
    }
    /**
     * A character's special attack
     */
    public int spAttack(){
        return 15;
    }
    /**
     * Returns the HP of a character
     * @return Description text text text.
     */
    public int getHP(){
        return HP;
    }
    /**
     * Reduces the HP of a character who has taken damage
     * updates the instance variable
     * @param  damage
     */
    public void takeDamage(int damage){
        HP = HP - damage;
    }
    /**
     * Checks to see if the player is able to move into the
     * location wanted
     */
    public void canMove(){

    }
}
