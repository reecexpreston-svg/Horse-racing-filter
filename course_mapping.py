"""
Course Characteristics Mapping for UK and Irish Racecourses
Maps each course to its Surface, Configuration, and LH/RH (Handedness)
"""

COURSE_CHARACTERISTICS = {
    # UK Courses - from Pattern Form official data
    "Aintree": {
        "surface": "Flat",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Left Handed"
    },
    "Ascot": {
        "surface": "Undulating",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Right Handed"
    },
    "Ayr": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Bangor-On-Dee": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Very Sharp",
        "lh_rh": "Left Handed"
    },
    "Bath": {
        "surface": "Undulating",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Left Handed"
    },
    "Beverley": {
        "surface": "Undulating",
        "configuration": "Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Brighton": {
        "surface": "Severe Undulations",
        "configuration": "Very Sharp",
        "lh_rh": "Left Handed"
    },
    "Carlisle": {
        "surface": "Undulating",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Cartmel": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Very Sharp",
        "lh_rh": "Left Handed"
    },
    "Catterick": {
        "surface": "Undulating",
        "configuration": "Very Sharp",
        "lh_rh": "Left Handed"
    },
    "Cheltenham": {
        "surface": "Severe Undulations",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Left Handed"
    },
    "Chelmsford (AW)": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Chepstow": {
        "surface": "Severe Undulations",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Left Handed"
    },
    "Chester": {
        "surface": "Flat",
        "configuration": "Very Sharp",
        "lh_rh": "Left Handed"
    },
    "Doncaster": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Epsom 5f - 8f": {
        "surface": "Severe Undl - mainly Downhill",
        "configuration": "Very Sharp",
        "lh_rh": "Left Handed"
    },
    "Epsom 9f - 12f": {
        "surface": "Severe Undl",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Left Handed"
    },
    "Exeter": {
        "surface": "Undulating",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Fakenham": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Sharp - Uphill Finish",
        "lh_rh": "Left Handed"
    },
    "Ffos Las": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Folkestone": {
        "surface": "Undulating",
        "configuration": "Sharp",
        "lh_rh": "Right Handed"
    },
    "Fontwell": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Very sharp - Uphill Finish",
        "lh_rh": "Left Handed"
    },
    "Goodwood": {
        "surface": "Severe Undl - mainly Downhill",
        "configuration": "Very Sharp",
        "lh_rh": "Right Handed"
    },
    "Great Leighs (AW)": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Hamilton": {
        "surface": "Severe Undulations",
        "configuration": "Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Haydock": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Hereford": {
        "surface": "Flat",
        "configuration": "Sharp",
        "lh_rh": "Right Handed"
    },
    "Hexham": {
        "surface": "Severe Undulations",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Left Handed"
    },
    "Huntingdon": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Right Handed"
    },
    "Kelso": {
        "surface": "Undulating",
        "configuration": "Very sharp - Uphill Finish",
        "lh_rh": "Left Handed"
    },
    "Kempton": {
        "surface": "Flat",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Right Handed"
    },
    "Leicester": {
        "surface": "Undulating",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Lingfield": {
        "surface": "Undulating",
        "configuration": "Sharp",
        "lh_rh": "Left Handed"
    },
    "Lingfield (AW)": {
        "surface": "Undulating",
        "configuration": "Sharp",
        "lh_rh": "Left Handed"
    },
    "Lingfield Old": {
        "surface": "Undulating - mainly Downhill",
        "configuration": "Sharp",
        "lh_rh": "Left Handed"
    },
    "Ludlow": {
        "surface": "Flat",
        "configuration": "Very Sharp",
        "lh_rh": "Right Handed"
    },
    "Market Raisen": {
        "surface": "Undulating",
        "configuration": "Sharp",
        "lh_rh": "Right Handed"
    },
    "Musselburgh": {
        "surface": "Flat",
        "configuration": "Sharp",
        "lh_rh": "Right Handed"
    },
    "Newbury": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Newcastle": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Newcastle (AW)": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Newmarket": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Newton Abbot": {
        "surface": "Flat",
        "configuration": "Very Sharp",
        "lh_rh": "Left Handed"
    },
    "Nottingham": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Perth": {
        "surface": "Flat",
        "configuration": "Very Sharp",
        "lh_rh": "Right Handed"
    },
    "Plumpton": {
        "surface": "Undulating",
        "configuration": "Sharp",
        "lh_rh": "Left Handed"
    },
    "Pontefract": {
        "surface": "Undulating",
        "configuration": "Uphill Finish",
        "lh_rh": "Left Handed"
    },
    "Redcar": {
        "surface": "Flat",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Left Handed"
    },
    "Ripon": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Right Handed"
    },
    "Salisbury": {
        "surface": "Undulating",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Right Handed"
    },
    "Sandown": {
        "surface": "Undulating",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Sedgefield": {
        "surface": "Undulating",
        "configuration": "Sharp - Uphill Finish",
        "lh_rh": "Left Handed"
    },
    "Southwell": {
        "surface": "Flat",
        "configuration": "Sharp",
        "lh_rh": "Left Handed"
    },
    "Southwell (AW)": {
        "surface": "Flat",
        "configuration": "Sharp",
        "lh_rh": "Left Handed"
    },
    "Stratford": {
        "surface": "Flat",
        "configuration": "Sharp",
        "lh_rh": "Left Handed"
    },
    "Taunton": {
        "surface": "Flat",
        "configuration": "Sharp",
        "lh_rh": "Right Handed"
    },
    "Thirsk": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Left Handed"
    },
    "Towcester": {
        "surface": "Severe Undulations",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Uttoxeter": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Warwick": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Sharp",
        "lh_rh": "Left Handed"
    },
    "Wetherby": {
        "surface": "Flat",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Left Handed"
    },
    "Wincanton": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Right Handed"
    },
    "Windsor": {
        "surface": "Flat",
        "configuration": "Sharp",
        "lh_rh": "Right Handed"
    },
    "Wolverhampton (AW)": {
        "surface": "Flat",
        "configuration": "Sharp",
        "lh_rh": "Left Handed"
    },
    "Worcester": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Yarmouth": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "York": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    
    # Irish Courses - from Pattern Form official data
    "Ballinrobe": {
        "surface": "Undulating",
        "configuration": "Very Sharp",
        "lh_rh": "Right Handed"
    },
    "Bellewstown": {
        "surface": "Undulating",
        "configuration": "Sharp",
        "lh_rh": "Left Handed"
    },
    "Clonmel": {
        "surface": "Severe Undulations",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Cork": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Right Handed"
    },
    "Curragh": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Galloping",
        "lh_rh": "Right Handed"
    },
    "Downpatrick": {
        "surface": "Severe Undulations",
        "configuration": "Very Sharp",
        "lh_rh": "Right Handed"
    },
    "Down Royal": {
        "surface": "Undulating",
        "configuration": "Galloping",
        "lh_rh": "Right Handed"
    },
    "Dundalk": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Fairyhouse": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Galloping",
        "lh_rh": "Right Handed"
    },
    "Galway": {
        "surface": "Severe Undulations",
        "configuration": "Sharp - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Gowran Park": {
        "surface": "Undulating",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Kilbeggan": {
        "surface": "Undulating",
        "configuration": "Very sharp - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Killarney": {
        "surface": "Flat",
        "configuration": "Galloping with Sharp bends",
        "lh_rh": "Left Handed"
    },
    "Laytown": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Leopardstown": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Limerick": {
        "surface": "Undulating",
        "configuration": "Galloping",
        "lh_rh": "Right Handed"
    },
    "Listowel": {
        "surface": "Flat",
        "configuration": "Very Sharp",
        "lh_rh": "Left Handed"
    },
    "Naas": {
        "surface": "Undulating",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Left Handed"
    },
    "Navan": {
        "surface": "Undulating",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Left Handed"
    },
    "Punchestown": {
        "surface": "Undulating",
        "configuration": "Galloping",
        "lh_rh": "Right Handed"
    },
    "Roscommon": {
        "surface": "Mainly flat with minor Undl",
        "configuration": "Sharp",
        "lh_rh": "Right Handed"
    },
    "Sligo": {
        "surface": "Severe Undulations",
        "configuration": "Very sharp - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Thurles": {
        "surface": "Undulating",
        "configuration": "Sharp",
        "lh_rh": "Right Handed"
    },
    "Tipperary": {
        "surface": "Flat",
        "configuration": "Galloping",
        "lh_rh": "Left Handed"
    },
    "Tramore": {
        "surface": "Severe Undulations",
        "configuration": "Very sharp - Uphill Finish",
        "lh_rh": "Right Handed"
    },
    "Wexford": {
        "surface": "Undulating",
        "configuration": "Galloping - Uphill Finish",
        "lh_rh": "Right Handed"
    }
}


def get_course_characteristics(course_name):
    """
    Get characteristics for a given course
    
    Args:
        course_name (str): Name of the racecourse
        
    Returns:
        dict: Dictionary with surface, configuration, and lh_rh keys
        Returns None if course not found
    """
    return COURSE_CHARACTERISTICS.get(course_name)


def add_characteristics_to_race(race_dict):
    """
    Add course characteristics to a race dictionary
    
    Args:
        race_dict (dict): Race dictionary with 'course' key
        
    Returns:
        dict: Race dictionary with added characteristics
    """
    course = race_dict.get('course')
    if course:
        characteristics = get_course_characteristics(course)
        if characteristics:
            race_dict.update(characteristics)
    return race_dict


def get_all_courses():
    """Get list of all courses with their characteristics"""
    return COURSE_CHARACTERISTICS


if __name__ == "__main__":
    # Test the mapping
    print("Total courses mapped:", len(COURSE_CHARACTERISTICS))
    print("\nExample - Cheltenham:")
    print(get_course_characteristics("Cheltenham"))
    print("\nExample - Ascot:")
    print(get_course_characteristics("Ascot"))
