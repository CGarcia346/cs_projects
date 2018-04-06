 /**
 * Autocompleter.java
 * Jeff Ondich, 20 March 2018
 * Carlos Garcia & Joey Cook-Gallardo
 * This class exposes a very simple interface for generating auto-completions of search strings.
 * The purpose of this class is to give the students in CS257 an opportunity to practice creating
 * unit tests.
 */
package edu.carleton.garciac3;

import jdk.internal.util.xml.impl.Input;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Autocompleter {

    public static void main(String[] args){
        Autocompleter run = new Autocompleter(args[0]);
        run.getCompletions(args[1]);
    }

    /**
     * @param dataFilePath the path to the data file containing the set of items to
     * from which auto-completed results will be drawn. (In the context of this assignment,
     * this will be the path to the actors.txt file I provided you. But we'll also talk
     * later about how you might use inheritance to create subclasses of Autocompleter
     * to use different datasets and different approaches to doing the autocompletion.)
     */
    private ArrayList<String> Actors = null;
    private ArrayList<String> searchList = null;

    public Autocompleter(String dataFilePath) {
        // Initialization goes here, as needed. For example, you might load
        // from a file into a list (or a hashmap or something like that)
        // the list of strings that are going to form the dataset of potential
        // auto-completions. The initialization will be up to you.
        Actors = new ArrayList<String>();
        File inputFile = new File(dataFilePath);
        Scanner scanner;
        try {
            scanner = new Scanner(inputFile);
        }
        catch (FileNotFoundException e){
            System.err.println(e);
            return;
        }
        while (scanner.hasNextLine()) {
            String Actor = scanner.nextLine();
            Actors.add(Actor);
        }
        }

    /**
     * @param searchString the string whose autocompletions are sought
     * @return the list of potential completions that match the search string,
     *  sorted in decreasing order of quality of the match (that is, the matches
     *  are sorted from best match to weakest match)
     */

    private void createFix(){
        searchList = new ArrayList<String>();
        int y = 0;
        while(y < Actors.size()){
            searchList.add(Actors.get(y).toLowerCase().replaceAll(" ", ""));
            y++;
        }
    }
    private List<String> transfer(List<String> rmv, List<String> onTo){
        while(!rmv.isEmpty()){
            onTo.add(rmv.remove(0));
        }
        return onTo;
    }
    private List<String> createOrder(List<String> toBeOrdered, String causeOrder){
        List<String> order = new ArrayList<String>();
        List<String> lower = new ArrayList<String>();

        int y = 0;
        while(y < toBeOrdered.size()){
            lower.add(toBeOrdered.get(y).toLowerCase().replaceAll(" ", ""));
            y++;
        }

        while(!toBeOrdered.isEmpty()){
            int toCompare = toBeOrdered.get(0).indexOf(causeOrder);
            int location = 0;
            int i = 0;

            while(i < toBeOrdered.size()){
                if(lower.get(i).indexOf(causeOrder) < toCompare){
                    location = i;
                    toCompare = lower.get(i).indexOf(causeOrder);
                }
                i++;
            }
            order.add(toBeOrdered.remove(location));
        }
        return order;
    }

    public List<String> getCompletions(String searchString){
        createFix();
        List<String> results = new ArrayList<String>();
        List<String> fPrio = new ArrayList<String>();
        List<String> sPrio = new ArrayList<String>();
        List<String> tPrio = new ArrayList<String>();
        List<String> lPrio = new ArrayList<String>();
        if(searchString.equals("")){
            System.out.println("You have entered nothing, Try Again!");
            return results;
        }
        String ss = searchString.toLowerCase().replaceAll(" ", "");

        int i = 0;
        while(i < searchList.size()){

            if(searchList.get(i).contains(ss)){
                String cur = searchList.get(i);
                //Check for last name priority
                if(ss.equals(cur.substring(0, ss.length()))){
                    fPrio.add(Actors.get(i));
                }
                //Check for first name priority
                else if(ss.equals(cur.substring(cur.indexOf(",")+1, cur.indexOf(",") + ss.length()+1))){
                    sPrio.add(Actors.get(i));
                }
                //Check for last name substring priority
                else if(cur.indexOf(",") > cur.indexOf(ss)){
                    tPrio.add(Actors.get(i));
                }
                //Check for first name substring priority
                else if(cur.indexOf(",") < cur.indexOf(ss)) {
                    lPrio.add(Actors.get(i));
                }
            }
            i++;
        }
        fPrio = createOrder(fPrio, ss);
        sPrio = createOrder(sPrio, ss);
        tPrio = createOrder(tPrio, ss);
        lPrio = createOrder(lPrio, ss);
        results = transfer(fPrio, results);
        results = transfer(sPrio, results);
        results = transfer(tPrio, results);
        results = transfer(lPrio, results);
        return results;
    }
    public static void main(String[] args) {
        Autocompleter run = new Autocompleter(args[0]);
        run.getCompletions(args[1]);
    }
}
