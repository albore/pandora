
#ifndef __MyVillage_hxx__
#define __MyVillage_hxx__

#include <vector>
#include <Point2D.hxx>

namespace GujaratCellphones
{

class MyVillage
{	
	std::vector<std::string> _citizens;
	int _id;
	Engine::Point2D<int> _location;

public:
	MyVillage();
	MyVillage(int id);
	virtual ~MyVillage();
	void addCitizen(const std::string & id);
	std::vector<std::string> getCitizens();
	int getId();
	Engine::Point2D<int> getLocation();
	bool isCitizenOfVillage(const std::string & id);
	void setLocation(const Engine::Point2D<int> &p);
};

} // namespace GujaratCellphones

#endif // __MyVillage_hxx__

