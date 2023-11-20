#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// NTP Clock
class NTPClock {
    private:
        double rate;
        double offset;
        double precision;
        int lastUpdate;
        int current_timestamp;
        int corrected_timestamp;

    public:

        NTPClock() {
            this->rate = 1.0;
            this->offset = 0.0;
            this->precision = 0.0;
            this->lastUpdate = 0;
            this->current_timestamp = 0;
            this->corrected_timestamp = 0;
        }

        double getRate() {
            return this->rate;
        }

        double getOffset() {
            return this->offset;
        }

        double getPrecision() {
            return this->precision;
        }

        int getLastUpdate() {
            return this->lastUpdate;
        }

        int getCurrentTimestamp() {
            return this->current_timestamp;
        }

        int getCorrectedTimestamp() {
            return this->corrected_timestamp;
        }

        void setRate(double rate) {
            this->rate = rate;
        }

        void setOffset(double offset) {
            this->offset = offset;
        }

        void setPrecision(double precision) {
            this->precision = precision;
        }

        void setLastUpdate(int lastUpdate) {
            this->lastUpdate = lastUpdate;
        }

        void upDateTimestamp() {
            this->current_timestamp = this->lastUpdate + (clock() - this->lastUpdate);
        }

        void correctTimestamp() {
            this->corrected_timestamp = this->current_timestamp * this->rate + this->offset;
        }
};


int main(){
    NTPClock clk = NTPClock();
    printf("Rate: %f\n", clk.getRate());
}