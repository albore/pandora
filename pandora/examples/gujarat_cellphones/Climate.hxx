#ifndef __Climate_hxx__
#define __Climate_hxx__

#include <boost/random.hpp>
#include <boost/random/gamma_distribution.hpp>

namespace GujaratCellphones {

class MyWorldConfig;

class Climate
{	
	typedef boost::mt19937 RandomEngine;
	RandomEngine _randomGenerator;
	float _currentRain; // mm on heigth of rain
	float _alphaRain;
	float _betaRain;

	boost::variate_generator< RandomEngine, boost::uniform_real<> > _uniformDistribution;
public:
	Climate(const MyWorldConfig &config);
	virtual ~Climate();

	const float & getRain() const;
	void computeRainValue();
};

}

#endif // __Climate_hxx__

