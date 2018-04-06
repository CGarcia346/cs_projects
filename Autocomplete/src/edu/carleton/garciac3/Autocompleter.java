 /**
 * Autocompleter.java
 * Jeff Ondich, 20 March 2018
 * Carlos Garcia & Joey Cook-Gallardo
 * This class exposes a very simple interface for generating auto-completions of search strings.
 */
 /*
 When we try to run using the command line and the package isn't commented out, the program
 will not run.
 */
//package edu.carleton.garciac3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Autocompleter {

    /**
     * @param dataFilePath the path to the data file containing the set of items to
     * from which auto-completed results will be drawn. (In the context of this assignment,
     * this will be the path to the actors.txt file I provided you. But we'll also talk
     * later about how you might use inheritance to create subclasses of Autocompleter
     * to use different datasets and different approaches to doing the autocompletion.)
     */
    private ArrayList<String> Actors;
    private ArrayList<String> searchList = null;

    public Autocompleter(String dataFilePath) {
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
     * a method that creates a new ArrayList with the actors in the actors.txt file
     * with the spaces removed and the Actors name turned to all lowercase
     */
    private void createFix(){
        searchList = new ArrayList<String>();
        int y = 0;
        while(y < Actors.size()){
            searchList.add(Actors.get(y).toLowerCase().replaceAll(" ", ""));
            y++;
        }
    }
    /**
     * A method to remove the contents of an ArrayList and place them into another ArrayList
     * @param List<String> rmv
     * @param List<String> onTo
     * @return an ArrayList
     */
    private List<String> transfer(List<String> rmv, List<String> onTo){
        while(!rmv.isEmpty()){
            onTo.add(rmv.remove(0));
        }
        return onTo;
    }
    /**
     * Organizes and returns A list of search results
     * @param List<String> toBeOrdered
     * @param String causeOrder
     * @return an ordered ArrayList
     */
    private List<String> createOrder(List<String> toBeOrdered, String causeOrder){
        List<String> order = new ArrayList<String>();
        List<String> lower = new ArrayList<String>();
        String co = causeOrder.toLowerCase().replaceAll(" ", "");
        int y = 0;
        while(y < toBeOrdered.size()){
            lower.add(toBeOrdered.get(y).toLowerCase().replaceAll(" ", ""));
            y++;
        }

        while(!toBeOrdered.isEmpty()){
            int toCompare = lower.get(0).indexOf(co);
            int location = 0;
            int i = 0;
            while(i < toBeOrdered.size()){
                if(lower.get(i).indexOf(co) < toCompare){
                    location = i;
                    toCompare = lower.get(i).indexOf(co);
                }
                i++;
            }
            order.add(toBeOrdered.remove(location));
        }
        return order;
    }

    /**
     * @param searchString the string whose autocompletions are sought
     * @return the list of potential completions that match the search string,
     *  sorted in decreasing order of quality of the match (that is, the matches
     *  are sorted from best match to weakest match)
     */

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
    /**
     * a main method that allows for a command line argument and prints back to user
     * @param
     */
    public static void main(String[] args) {
        Autocompleter run = new Autocompleter(args[0]);
        List<String> show = run.getCompletions(args[1]);
        for(int i = 0; i < show.size(); i++){
            System.out.println(show.get(i));
        }

    }
}
