/**
 * Carlos Garcia & Joey Cook-Gallardo 3 April, 2018
 * Professor Jeffrey Ondich
 *
 */


package edu.carleton.garciac3;

import static org.junit.jupiter.api.Assertions.*;
import java.util.List;

class AutocompleterTest {

    Autocompleter completer = null;

    @org.junit.jupiter.api.BeforeEach
    void setUp() {
        completer = new Autocompleter("actors.txt");
    }

    @org.junit.jupiter.api.AfterEach
    void tearDown() {
        completer = null;
    }

    @org.junit.jupiter.api.Test
    void checkEmpty() {
        List<String> emptyCompletions = completer.getCompletions("Seinfeld, Jerry");
        String[] empty = {};
        String[] arrayEmpty = emptyCompletions.toArray(new String [0]);
        assertArrayEquals(empty, arrayEmpty, "Empty Arrays wanted!");
    }

    /*@org.junit.jupiter.api.Test
    void checkNull(){
        List<String> completions = completer.getCompletions("");
        String[] nothing = {""};
        assertArrayEquals(nothing, completions.toArray(), "Empty Arrays wanted!");
    }*/

    @org.junit.jupiter.api.Test
    void lSearch(){
        List<String> completions = completer.getCompletions("Huston");
        String[] expected = {"Huston, Anjelica", "Huston, Walter"};
        String[] arrayCompletions = completions.toArray(new String [0]);
        assertArrayEquals(expected, arrayCompletions, "Last-name search generated wrong results");
    }

    @org.junit.jupiter.api.Test
    void fSearch(){
        List<String> fComp = completer.getCompletions("Gloria");
        String[] expected = {"Grahame, Gloria", "Stuart, Gloria", "Swanson, Gloria"};
        String[] arrayCompletions = fComp.toArray(new String [0]);
        assertArrayEquals(expected, arrayCompletions, "first-name search generated wrong results");
    }

    @org.junit.jupiter.api.Test
    void lSubSearch(){
        List<String> lSubCompletions = completer.getCompletions("rig");
        String[] expected = {"Riggle, Rob", "Wright, Jeffrey", "Wright, Robin",
                "Wright, Teresa",  "Rodriguez, Michelle"};
        String[] arrayCompletions = lSubCompletions.toArray(new String [0]);
        assertArrayEquals(expected, arrayCompletions, "last-name substring search generated wrong results");
    }

    @org.junit.jupiter.api.Test
    void fSubSearch(){
        List<String> fSubCompletions = completer.getCompletions("Toni");
        String[] expected = {"Collette, Toni", "Banderas, Antonio"};
        String[] arrayCompletions = fSubCompletions.toArray(new String [0]);
        assertArrayEquals(expected, arrayCompletions, "first-name substring search generated wrong results");
    }

    @org.junit.jupiter.api.Test
    void mSearch(){
        List<String> midCompletions = completer.getCompletions("az");
        String[] expected = {"Diaz, Cameron", "Barraza, Adriana", "Palminteri, Chazz"};
        String[] arrayCompletions = midCompletions.toArray(new String [0]);
        assertArrayEquals(expected, arrayCompletions, "Substring cross search generated wrong results");
    }

    @org.junit.jupiter.api.Test
    void checkPerfectSearch(){
        List<String> orderC = completer.getCompletions("cla");
        String[] correctOrder = {"Clarke, Emilia", "Clarkson, Patricia", "Clayburgh, Jill", "Cardinale, Claudia",
                "Colbert, Claudette", "Danes, Claire", "Gable, Clark", "Gregg, Clark","Rains, Claude", "Trevor, Claire",
                "MacLaine, Shirley", "McLaglen, Victor", "Duncan, Michael Clarke",  "Van Damme, Jean-Claude"};
        String[] orderArray = orderC.toArray(new String [0]);
        assertArrayEquals(correctOrder, orderArray, "Incorrect Orrder");
    }

    @org.junit.jupiter.api.Test
    void checkQBee(){
        List<String> singles = completer.getCompletions("Bey");
        String[] qBee = {"Beyoncé", "Maguire, Tobey"};
        assertArrayEquals(qBee, singles.toArray(), "You failed Beyonce");
    }
}