# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from neutron_lib.api.definitions import address_scope
from neutron_lib.api.definitions import agent
from neutron_lib.api.definitions import allowedaddresspairs
from neutron_lib.api.definitions import auto_allocated_topology
from neutron_lib.api.definitions import availability_zone
from neutron_lib.api.definitions import availability_zone_filter
from neutron_lib.api.definitions import bgpvpn
from neutron_lib.api.definitions import bgpvpn_routes_control
from neutron_lib.api.definitions import bgpvpn_stdattrs
from neutron_lib.api.definitions import bgpvpn_stdattrs_net_assoc
from neutron_lib.api.definitions import bgpvpn_stdattrs_port_assoc
from neutron_lib.api.definitions import bgpvpn_stdattrs_router_assoc
from neutron_lib.api.definitions import bgpvpn_vni
from neutron_lib.api.definitions import data_plane_status
from neutron_lib.api.definitions import default_subnetpools
from neutron_lib.api.definitions import dhcpagentscheduler
from neutron_lib.api.definitions import dns
from neutron_lib.api.definitions import dns_domain_ports
from neutron_lib.api.definitions import dvr
from neutron_lib.api.definitions import empty_string_filtering
from neutron_lib.api.definitions import expose_port_forwarding_in_fip
from neutron_lib.api.definitions import external_net
from neutron_lib.api.definitions import extra_dhcp_opt
from neutron_lib.api.definitions import extraroute
from neutron_lib.api.definitions import filter_validation
from neutron_lib.api.definitions import fip64
from neutron_lib.api.definitions import fip_port_details
from neutron_lib.api.definitions import firewall
from neutron_lib.api.definitions import firewall_v2
from neutron_lib.api.definitions import firewallrouterinsertion
from neutron_lib.api.definitions import flavors
from neutron_lib.api.definitions import floating_ip_port_forwarding
from neutron_lib.api.definitions import floatingip_pools
from neutron_lib.api.definitions import flowclassifier
from neutron_lib.api.definitions import ip_allocation
from neutron_lib.api.definitions import ip_substring_port_filtering
from neutron_lib.api.definitions import l2_adjacency
from neutron_lib.api.definitions import l3
from neutron_lib.api.definitions import l3_ext_gw_mode
from neutron_lib.api.definitions import l3_ext_ha_mode
from neutron_lib.api.definitions import l3_flavors
from neutron_lib.api.definitions import logging
from neutron_lib.api.definitions import logging_resource
from neutron_lib.api.definitions import metering
from neutron_lib.api.definitions import multiprovidernet
from neutron_lib.api.definitions import network
from neutron_lib.api.definitions import network_availability_zone
from neutron_lib.api.definitions import network_ip_availability
from neutron_lib.api.definitions import network_mtu
from neutron_lib.api.definitions import network_mtu_writable
from neutron_lib.api.definitions import pagination
from neutron_lib.api.definitions import port
from neutron_lib.api.definitions import port_mac_address_regenerate
from neutron_lib.api.definitions import port_security
from neutron_lib.api.definitions import portbindings
from neutron_lib.api.definitions import portbindings_extended
from neutron_lib.api.definitions import project_id
from neutron_lib.api.definitions import provider_net
from neutron_lib.api.definitions import qos
from neutron_lib.api.definitions import qos_bw_limit_direction
from neutron_lib.api.definitions import qos_bw_minimum_ingress
from neutron_lib.api.definitions import qos_default
from neutron_lib.api.definitions import qos_rule_type_details
from neutron_lib.api.definitions import revisionifmatch
from neutron_lib.api.definitions import router_availability_zone
from neutron_lib.api.definitions import router_interface_fip
from neutron_lib.api.definitions import routerservicetype
from neutron_lib.api.definitions import security_groups_port_filtering
from neutron_lib.api.definitions import segment
from neutron_lib.api.definitions import segments_peer_subnet_host_routes
from neutron_lib.api.definitions import servicetype
from neutron_lib.api.definitions import sfc
from neutron_lib.api.definitions import sort_key_validation
from neutron_lib.api.definitions import sorting
from neutron_lib.api.definitions import standard_attr_segment
from neutron_lib.api.definitions import subnet
from neutron_lib.api.definitions import subnet_onboard
from neutron_lib.api.definitions import subnet_segmentid_writable
from neutron_lib.api.definitions import subnetpool
from neutron_lib.api.definitions import trunk
from neutron_lib.api.definitions import trunk_details
from neutron_lib.api.definitions import uplink_status_propagation
from neutron_lib.api.definitions import vlantransparent
from neutron_lib.api.definitions import vpn
from neutron_lib.api.definitions import vpn_endpoint_groups
from neutron_lib.api.definitions import vpn_flavors


_ALL_API_DEFINITIONS = {
    address_scope,
    agent,
    allowedaddresspairs,
    auto_allocated_topology,
    availability_zone,
    availability_zone_filter,
    bgpvpn,
    bgpvpn_routes_control,
    bgpvpn_stdattrs,
    bgpvpn_stdattrs_net_assoc,
    bgpvpn_stdattrs_port_assoc,
    bgpvpn_stdattrs_router_assoc,
    bgpvpn_vni,
    data_plane_status,
    default_subnetpools,
    dhcpagentscheduler,
    dns,
    dns_domain_ports,
    dvr,
    empty_string_filtering,
    expose_port_forwarding_in_fip,
    external_net,
    extra_dhcp_opt,
    extraroute,
    filter_validation,
    fip64,
    firewall,
    firewall_v2,
    firewallrouterinsertion,
    fip_port_details,
    flavors,
    floating_ip_port_forwarding,
    floatingip_pools,
    ip_allocation,
    ip_substring_port_filtering,
    l2_adjacency,
    flowclassifier,
    l3,
    l3_ext_gw_mode,
    l3_ext_ha_mode,
    l3_flavors,
    logging,
    logging_resource,
    metering,
    multiprovidernet,
    network,
    network_availability_zone,
    network_ip_availability,
    network_mtu,
    network_mtu_writable,
    pagination,
    port,
    port_mac_address_regenerate,
    port_security,
    portbindings,
    portbindings_extended,
    project_id,
    provider_net,
    qos,
    qos_bw_limit_direction,
    qos_bw_minimum_ingress,
    qos_default,
    qos_rule_type_details,
    revisionifmatch,
    router_availability_zone,
    router_interface_fip,
    routerservicetype,
    security_groups_port_filtering,
    segment,
    segments_peer_subnet_host_routes,
    servicetype,
    sfc,
    sort_key_validation,
    sorting,
    standard_attr_segment,
    subnet,
    subnet_onboard,
    subnet_segmentid_writable,
    subnetpool,
    trunk,
    trunk_details,
    uplink_status_propagation,
    vlantransparent,
    vpn,
    vpn_endpoint_groups,
    vpn_flavors,
}
