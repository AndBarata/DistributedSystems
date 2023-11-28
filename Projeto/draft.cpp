#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h> 
#include <iostream>


// NTP Clock
class NTPClock {
    private:
        double rate; // The rate of the clock
        double offset; // The offset of the clock
        double precision; // The precision of the clock
        int lastUpdate; // The last update time of the clock
        int current_timestamp; // The current timestamp of the clock
        int corrected_timestamp; // The corrected timestamp of the clock

    public:

        // Constructor
        // Initializes all attributes to their default values
        NTPClock() {
            this->rate = 1.0;
            this->offset = 0.0;
            this->precision = 0.0;
            this->lastUpdate = 0;
            this->current_timestamp = 0;
            this->corrected_timestamp = 0;
        }

        // Getters and Setters

        // Returns the rate of the clock
        double getRate() {
            return this->rate;
        }

        // Returns the offset of the clock
        double getOffset() {
            return this->offset;
        }

        // Returns the precision of the clock
        double getPrecision() {
            return this->precision;
        }

        // Returns the last update time of the clock
        int getLastUpdate() {
            return this->lastUpdate;
        }

        // Returns the current timestamp of the clock
        int getCurrentTimestamp() {
            return this->current_timestamp;
        }

        // Returns the corrected timestamp of the clock
        int getCorrectedTimestamp() {
            return this->corrected_timestamp;
        }

        // Sets the rate of the clock
        void setRate(double rate) {
            this->rate = rate;
        }

        // Sets the offset of the clock
        void setOffset(double offset) {
            this->offset = offset;
        }

        // Sets the precision of the clock
        void setPrecision(double precision) {
            this->precision = precision;
        }

        // Sets the last update time of the clock
        void setLastUpdate(int lastUpdate) {
            this->lastUpdate = lastUpdate;
        }

        // Updates the current timestamp incrementally
        // The new timestamp is the sum of the last update time and the difference between the current clock time and the last update time
        void incrementTimestamp() {
            this->current_timestamp = this->lastUpdate + (clock() - this->lastUpdate);
        }

        // Corrects the timestamp with the offset and rate
        // The corrected timestamp is the product of the current timestamp and the rate, plus the offset
        void correctTimestamp() {
            this->corrected_timestamp = this->current_timestamp * this->rate + this->offset;
        }
};


int main(){
    NTPClock clk = NTPClock();
    int last_clk = clock();
    sync_rate = 10;

    for (int i=0; i<100; i++){
        //clk.upDateTimestamp();
        if last_clk - clk.current_timestamp >= sync_:
        clk.incrementTimestamp();
        printf(" [%d] Clock: %d\n", i, clk.getCurrentTimestamp()-last_clk);
        last_clk = clk.getCurrentTimestamp();
        
    }
}