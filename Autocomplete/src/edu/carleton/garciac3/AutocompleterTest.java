package edu.carleton.garciac3;

import static org.junit.jupiter.api.Assertions.*;

class AutocompleterTest {

    @org.junit.jupiter.api.BeforeEach
    void setUp() {
        Autocompleter autocompleter = new Autocompleter("actors.txt");
    }

    @org.junit.jupiter.api.AfterEach
    void tearDown() {
    }

    @org.junit.jupiter.api.Test
    void getCompletions() {
    }
}