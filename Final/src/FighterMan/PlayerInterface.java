package FighterMan;

public interface PlayerInterface{

    public int attack();
    public int spAttack();
    public void move(int row, int column);
    public void takeDamage(int damage);
}
