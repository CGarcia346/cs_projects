package sample;

import java.util.*;
import java.util.Random;

public class Player implements PlayerInterface{

    private int HP  = 100;
    private int row;
    private int column;
    private boolean dead;

    public void move(int row, int column){

    }

    public int attack(){
        return 25;
    }

    public int spAttack(){
        return 15;
    }

    public int getHP(){
        return HP;
    }

    public void takeDamage(int damage){
        HP = HP - damage;
    }

    public void canMove(){

    }
}
